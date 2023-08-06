from datetime import datetime
import tempfile
try:
    import mock
except ImportError:
    from unittest import mock

import click
from click.testing import CliRunner
from tinydb import TinyDB
from tinydb.storages import MemoryStorage
import pytest

from passpie import cli, completion
from passpie.crypt import FileExistsError


@pytest.fixture
def mock_cfg(mocker):
    tmpdir = tempfile.mkdtemp()
    config = cli.config
    config.path = tmpdir
    mocker.patch('passpie.cli.load_config', return_value=config)
    return config


@pytest.fixture
def mock_db(mocker, mock_cfg):
    mocker.patch('passpie.cli.ensure_is_database')
    credentials = [
        {'login': 'foo', 'name': 'bar', 'fullname': 'foo@bar',
         'password': '', 'comment': ''},
        {'login': 'foa', 'name': 'bazzy', 'fullname': 'foa@bazzy',
         'password': '', 'comment': ''},
        {'login': 'spam', 'name': 'egg', 'fullname': 'spam@egg',
         'password': '', 'comment': ''},
    ]
    database = TinyDB(storage=MemoryStorage)
    database.insert_multiple(credentials)
    MockDB = mock.MagicMock(return_value=database)
    mocker.patch('passpie.cli.Database', MockDB)
    return database


@pytest.fixture
def mock_cryptor(mocker, mock_cfg):
    mock_cryptor = mock.MagicMock()
    mock_cryptor_context = mocker.patch("passpie.cli.Cryptor")
    mock_cryptor_context().__enter__.return_value = mock_cryptor
    return mock_cryptor


def test_cli_search_find_results_by_login_regex(mock_db):
    runner = CliRunner()
    result = runner.invoke(cli.search, ['fo[oa]'])

    assert result.exit_code == 0
    assert 'foo' in result.output
    assert 'foa' in result.output
    assert 'spam' not in result.output


def test_cli_remove_delete_credential_found_by_database(mock_db):
    runner = CliRunner()
    result = runner.invoke(cli.remove, ['foo@bar'], input='y')
    result_print = runner.invoke(cli.cli)

    assert result.exit_code == 0
    assert 'foo' not in result_print.output


def test_cli_copy_credential_password_to_clipboard(mocker, mock_db, mock_cryptor):
    fullname = 'foo@bar'
    password = 's3cr3t'
    mocker.patch('passpie.cli.ensure_passphrase')
    mock_clipboard = mocker.patch('passpie.cli.clipboard')
    mock_cryptor.decrypt.return_value = password
    runner = CliRunner()
    result = runner.invoke(cli.copy, [fullname], input='passphrase')

    assert result.exit_code == 0
    assert mock_clipboard.copy.called
    mock_clipboard.copy.assert_called_once_with(password)


def test_cli_reset_database_overwrite_old_keys(mocker, mock_db, mock_cryptor):
    mocker.patch('passpie.cli.ensure_passphrase')
    new_passphrase = mocker.patch('passpie.cli.click.prompt')()

    runner = CliRunner()
    result = runner.invoke(cli.reset, input='passphrase')

    assert result.exit_code == 0
    assert mock_cryptor.create_keys.called
    mock_cryptor.create_keys.assert_called_once_with(
        new_passphrase, overwrite=True)


def test_cli_reset_database_re_encrypt_all_passwords(mocker, mock_db, mock_cryptor):
    password = 's3cr3t'
    mocker.patch('passpie.cli.ensure_passphrase')
    mocker.patch('passpie.cli.Cryptor.create_keys')
    mocker.patch('passpie.cli.click.prompt')
    mock_cryptor.decrypt.return_value = password

    runner = CliRunner()
    result = runner.invoke(cli.reset, input='passphrase')

    assert result.exit_code is 0
    assert mock_cryptor.encrypt.call_count is len(mock_db.all())
    assert mock_cryptor.decrypt.call_count is len(mock_db.all())
    for credential in mock_db.all():
        mock_cryptor.decrypt.assert_any_call_with(credential['password'])
    for credential in mock_db.all():
        mock_cryptor.encrypt.assert_any_call_with(password)


def test_cli_reset_purges_all_elements(mocker, mock_db, mock_cryptor):
    mocker.patch('passpie.cli.ensure_passphrase')
    mocker.patch('passpie.cli.click.prompt')
    mocker.patch.object(mock_db, 'purge')

    runner = CliRunner()
    result = runner.invoke(cli.reset, input='passphrase')

    assert result.exit_code is 0
    assert mock_db.purge.called


def test_init_success(mocker, mock_cryptor):
    mocker.patch('passpie.cli.Repository')
    passphrase = "PASS2pie"
    runner = CliRunner()
    result = runner.invoke(cli.init, ["--passphrase", passphrase])
    expected_msg = "Initialized database in {}\n".format(cli.config.path)

    assert result.output == expected_msg
    mock_cryptor.create_keys.assert_called_once_with(passphrase)


def test_init_prints_error_when_keys_exist(mocker, mock_cryptor):
    mocker.patch('passpie.cli.Repository')
    mock_cryptor.create_keys.side_effect = FileExistsError
    passphrase = "PASS2pie"
    path = cli.config.path
    message = 'Error: Database exists in %s. `--force` to overwrite\n' % path

    runner = CliRunner()
    result = runner.invoke(cli.init, ["--passphrase", passphrase])

    assert result.exit_code is not 0
    assert result.output == message


def test_init_has_success_when_keys_exits_and_force_is_passed(mocker, mock_cryptor):
    mocker.patch('passpie.cli.Repository')
    mock_shutil = mocker.patch('passpie.cli.shutil')
    passphrase = "PASS2pie"

    runner = CliRunner()
    result = runner.invoke(cli.init, ["--passphrase", passphrase, '--force'])

    assert result.exit_code is 0
    assert mock_shutil.rmtree.called
    mock_shutil.rmtree.assert_called_once_with(cli.config.path)


def test_copy_decrypts_password(mocker, mock_cryptor):
    mock_clipboard = mocker.patch('passpie.cli.clipboard')
    mocker.patch('passpie.cli.get_credential_or_abort')
    mocker.patch('passpie.cli.ensure_passphrase')
    fullname = "foo@bar"
    passphrase = "passphrase"
    mock_password = mock_cryptor.decrypt()

    runner = CliRunner()
    result = runner.invoke(cli.copy, [fullname, "--passphrase", passphrase])

    assert result.exit_code is 0
    mock_clipboard.copy.assert_called_once_with(mock_password)


def test_import_prints_nothing_when_no_importer_is_found(mocker, mock_cryptor):
    mocker.patch('passpie.cli.find_importer', return_value=None)

    runner = CliRunner()
    result = runner.invoke(cli.import_database, ['~/something'])

    assert result.exit_code is 0


def test_import_reencrypt_all_credential_passwords(mocker, mock_cryptor):
    password = 's3cret'
    credentials = [{'password': password}]
    mocker.patch('passpie.cli.Database')
    mock_importer = mocker.patch('passpie.cli.find_importer')()
    mock_importer.handle.return_value = credentials

    runner = CliRunner()
    result = runner.invoke(cli.import_database, ['something'])

    assert result.exit_code is 0
    assert mock_cryptor.encrypt.called is True
    mock_cryptor.encrypt.assert_called_once_with(password)


def test_search_prints_all_matched_search_credentials(mocker, mock_db):
    mock_db.search = mock.Mock(return_value=mock_db.all())
    mock_print_table = mocker.patch('passpie.cli.print_table')

    runner = CliRunner()
    result = runner.invoke(cli.search, ['pattern'])

    assert result.exit_code is 0
    mock_print_table.assert_called_once_with(mock_db.all())


def test_add_results_in_error_when_invalid_fullname(mocker, mock_db):
    mocker.patch('passpie.cli.split_fullname', side_effect=ValueError)

    runner = CliRunner()
    result = runner.invoke(cli.add, ['**bad**fullname', '--random'])

    assert result.exit_code is not 0
    assert result.output == 'Error: invalid fullname syntax\n'


def test_add_results_in_error_when_credential_already_exists(mocker, mock_db):
    message = 'Error: Credential foo@bar already exists. --force to overwrite\n'
    mocker.patch('passpie.cli.split_fullname', return_value=('foo', 'bar'))
    mock_db.get = mock.Mock(return_value=['found credential'])

    runner = CliRunner()
    result = runner.invoke(cli.add, ['foo@bar', '--random'])

    assert result.exit_code is not 0
    assert result.output == message


def test_get_credential_or_abort_sets_query_as_name(mocker, mock_db):
    credential = {'name': 'fake_name'}
    fullname = 'fullname'
    mocker.patch('passpie.cli.split_fullname', side_effect=ValueError)
    mock_where = mocker.patch('passpie.cli.where')
    mocker.patch.object(mock_db, 'get', return_value=credential)
    mocker.patch.object(mock_db, 'count', return_value=1)

    result = cli.get_credential_or_abort(mock_db, fullname)

    assert result == credential
    assert mock_db.get.called
    mock_db.get.assert_called_once_with(mock_where('name') == fullname)


def test_get_credential_or_abort_errors_on_credential_not_found(mocker, mock_db):
    mocker.patch.object(mock_db, 'get', return_value=None)

    with pytest.raises(click.ClickException) as excinfo:
        cli.get_credential_or_abort(mock_db, 'foo@bar')

    assert 'not found' in excinfo.value.message


def test_get_credential_or_abort_errors_on_multiple_credentials(mocker, mock_db):
    mocker.patch.object(mock_db, 'get', return_value=[{}])
    mocker.patch.object(mock_db, 'count', return_value=10)

    with pytest.raises(click.ClickException) as excinfo:
        cli.get_credential_or_abort(mock_db, 'foo@bar')

    assert 'Multiple matches' in excinfo.value.message


def test_add_credential_dont_exit_with_error_when_force(mocker, mock_db, mock_cryptor):
    mocker.patch.object(mock_db, 'get', return_value={'name': 'foo'})
    mocker.patch.object(mock_db, 'insert')

    runner = CliRunner()
    result = runner.invoke(cli.add, ['foo@bar', '--random', '--force'])

    assert result.exit_code is 0
    assert mock_db.insert.called


def test_raises_exception_when_gpg_not_installed(mocker):
    mocker.patch('passpie.utils.which', return_value=None)
    message = 'Error: GnuPG not installed. https://www.gnupg.org/\n'

    runner = CliRunner()
    result = runner.invoke(cli.cli)

    assert result.exit_code != 0
    assert result.output == message


def test_ensure_database_raises_error_when_path_is_not_dir(mocker):
    mocker.patch('passpie.cli.os.path.isdir', return_value=False)

    with pytest.raises(click.ClickException) as excinfo:
        cli.ensure_is_database('path')

    assert 'Not initialized database' in excinfo.value.message


def test_ensure_database_raises_error_when_path_is_not_valid(mocker):
    mocker.patch('passpie.cli.os.path.isdir', return_value=True)
    mocker.patch('passpie.cli.os.path.isfile', return_value=False)

    with pytest.raises(click.ClickException) as excinfo:
        cli.ensure_is_database('path')

    assert 'Not initialized database' in excinfo.value.message


def test_ensure_database_returns_none_when_valid_database(mocker):
    mocker.patch('passpie.cli.os.path.isdir', return_value=True)
    mocker.patch('passpie.cli.os.path.isfile', return_value=True)

    result = cli.ensure_is_database('path')

    assert result is None


def test_ensure_passphrase_raises_wrong_passphrase(mocker, mock_db, mock_cryptor):
    mock_cryptor.check.side_effect = ValueError
    mock_db._storage.path = 'path'

    with pytest.raises(click.ClickException) as excinfo:
        cli.ensure_passphrase(mock_db, 'passphrase')

    assert 'Wrong passphrase' in excinfo.value.message


def test_ensure_passphrase_returns_passphrase(mocker, mock_db, mock_cryptor):
    mock_db._storage.path = 'path'
    mock_cryptor.check.return_value = True
    passphrase = 'passphrase'

    result = cli.ensure_passphrase(mock_db, 'passphrase')

    assert result == passphrase


def test_update_dont_prompt_when_any_option_passed(mocker, mock_db, mock_cryptor):
    credential = {
        'fullname': 'foo@bar',
        'name': 'bar',
        'login': 'foo',
        'password': 's3cr3t',
        'comment': '',
        'modified': datetime.now(),
    }
    mock_prompt = mocker.patch('passpie.cli.click.prompt')
    mocker.patch('passpie.cli.get_credential_or_abort',
                 return_value=credential)

    runner = CliRunner()
    result = runner.invoke(cli.update, ['foo@bar', '--random'])

    assert result.exit_code == 0
    assert not mock_prompt.called


def test_update_prompt_input_for_each_editable_field(mocker, mock_db, mock_cryptor):
    credential = {
        'fullname': 'foo@bar',
        'name': 'bar',
        'login': 'foo',
        'password': 's3cr3t',
        'comment': '',
        'modified': datetime.now(),
    }
    mock_prompt = mocker.patch('passpie.cli.click.prompt',
                               return_value='')
    mock_make_fullname = mocker.patch('passpie.cli.make_fullname',
                                      return_value='foo@bar')
    mocker.patch('passpie.cli.get_credential_or_abort',
                 return_value=credential)

    runner = CliRunner()
    result = runner.invoke(cli.update, ['foo@bar'])

    assert result.exit_code == 0
    assert mock_prompt.call_count == 4
    assert mock_make_fullname.called


def test_remove_dont_ask_confimation_when_yes_passed(mocker, mock_db):
    mocker.patch.object(mock_db, 'remove')
    mock_confirm = mocker.patch('passpie.cli.click.confirm')

    runner = CliRunner()
    result = runner.invoke(cli.remove, ['foo@bar', '--yes'])

    assert result.exit_code == 0
    assert mock_confirm.called is False


def test_add_with_copy_option_add_pass_to_clipboard(mocker, mock_db, mock_cryptor):
    mock_clipboard = mocker.patch('passpie.cli.clipboard')

    runner = CliRunner()
    result = runner.invoke(cli.add, ['john.doe@spam', '--random', '--copy'])

    assert result.exit_code == 0
    assert mock_clipboard.copy.called


def test_remove_credentials_in_bulk(mocker, mock_db):
    credentials = [
        {'fullname': 'foo@bar'},
        {'fullname': 'foozy@bar'}
    ]
    mocker.patch.object(mock_db, 'remove')
    mocker.patch('passpie.cli.get_credential_or_abort',
                 return_value=credentials)

    runner = CliRunner()
    result = runner.invoke(cli.remove, ['foo@bar', '--yes'])

    assert result.exit_code == 0
    assert mock_db.remove.called
    assert mock_db.remove.call_count == 2


def test_cli_complete_chooses_bash_when_bash_passed_to_eval(mocker):
    mock_click = mocker.patch('passpie.cli.click')

    runner = CliRunner()
    result = runner.invoke(cli.complete, ['bash'])

    assert result.exit_code == 0
    assert mock_click.echo.called is True


def test_cli_complete_chooses_zsh_when_bash_passed_to_eval(mocker):
    mock_sys = mocker.patch('passpie.cli.sys')
    mock_click = mocker.patch('passpie.cli.click')

    runner = CliRunner()
    result = runner.invoke(cli.complete, ['bash'])

    assert result.exit_code == 0
    assert mock_click.echo.called is True


def test_cli_complete_chooses_prints_nothing_when_not_supported(mocker):
    mock_click = mocker.patch('passpie.cli.click')

    runner = CliRunner()
    result = runner.invoke(cli.complete, ['bash'])

    assert result.exit_code == 0
    assert mock_click.echo.called is True


def test_update_password_from_prompt_encrypts_password(mocker, mock_cryptor, mock_db):
    credential = {
        'fullname': 'foo@bar',
        'name': 'bar',
        'login': 'foo',
        'password': 's3cr3t',
        'comment': '',
        'modified': datetime.now(),
    }
    chosen_password = 'another_password'
    prompt_values = [
        credential['name'],
        credential['login'],
        chosen_password,  # password
        chosen_password,  # repeat password
        credential['comment'],
    ]
    mock_prompt = mocker.patch('passpie.cli.click.prompt',
                               side_effect=prompt_values)
    mock_make_fullname = mocker.patch('passpie.cli.make_fullname',
                                      return_value='foo@bar')
    mocker.patch('passpie.cli.get_credential_or_abort',
                 return_value=credential)
    mock_cryptor.encrypt.return_value = 'encrypted'

    runner = CliRunner()
    result = runner.invoke(cli.update, ['foo@bar'])

    assert result.exit_code == 0
    assert mock_cryptor.encrypt.called
    mock_cryptor.encrypt.assert_called_once_with(chosen_password)


def test_log_with_reset_to_pass_reset_to_number_to_git_reset(mocker):
    mocker.patch('passpie.cli.ensure_dependencies')
    MockRepository = mocker.patch('passpie.cli.Repository')
    mock_logger = mocker.patch('passpie.cli.logger')
    mock_repo = MockRepository()
    index = 0

    runner = CliRunner()
    result = runner.invoke(cli.log, ['--reset-to', index])

    assert result.exit_code == 0
    mock_repo.reset.assert_called_once_with(index)
    assert mock_logger.debug.called


def test_log_with_init_call_git_init_on_path(mocker):
    mocker.patch('passpie.cli.ensure_dependencies')
    MockRepository = mocker.patch('passpie.cli.Repository')
    mock_logger = mocker.patch('passpie.cli.logger')
    mock_repo = MockRepository()
    index = 0

    runner = CliRunner()
    result = runner.invoke(cli.log, ['--init'])

    assert result.exit_code == 0
    assert mock_repo.init.called
    assert mock_logger.debug.called


def test_log_prints_commit_list_when_not_option_is_passed(mocker):
    mocker.patch('passpie.cli.ensure_dependencies')
    MockRepository = mocker.patch('passpie.cli.Repository')
    mock_logger = mocker.patch('passpie.cli.logger')
    mock_repo = MockRepository()
    commits = [
        (2, mocker.MagicMock(message='Third commit')),
        (1, mocker.MagicMock(message='Second commit')),
        (0, mocker.MagicMock(message='First commit'))
    ]
    index = 0
    MockRepository().commit_list.return_value = commits

    runner = CliRunner()
    result = runner.invoke(cli.log)

    assert result.exit_code == 0
    for index, commit in commits:
        assert "[{}] {}".format(index, commit.message) in result.output


def test_cli_set_config_database_if_database_option_passed(mocker):
    path = '/path/to/database'
    mocker.patch('passpie.cli.ensure_dependencies')
    mocker.patch('passpie.cli.ensure_is_database')
    mocker.patch('passpie.cli.Database')
    mocker.patch('passpie.cli.click.Path', new_callable=str)
    mock_config = mocker.patch('passpie.cli.config')

    runner = CliRunner()
    result = runner.invoke(cli.cli, ['--database', path])

    assert result.exit_code == 0
    assert mock_config.path == path


def test_cli_set_logger_level_to_debug_when_verbose_option(mocker):
    mocker.patch('passpie.cli.ensure_dependencies')
    mocker.patch('passpie.cli.ensure_is_database')
    mock_logger = mocker.patch('passpie.cli.logger')

    runner = CliRunner()
    result = runner.invoke(cli.cli, ['--verbose'])

    assert mock_logger.setLevel.called
    mock_logger.setLevel.assert_called_once_with(cli.logging.DEBUG)


def test_cli_copy_to_stdout_with_to_stdout_option(mocker, mock_cryptor):
    credential = {
        'password': 's3cr3t'
    }
    mocker.patch('passpie.cli.ensure_passphrase')
    mocker.patch('passpie.cli.Database')
    mocker.patch('passpie.cli.get_credential_or_abort',
                 return_value=credential)
    mock_cryptor.decrypt.return_value = credential['password']

    runner = CliRunner()
    result = runner.invoke(
        cli.copy,
        ['foo@bar', '--to', 'stdout', '--passphrase', 'passphrase']
    )

    print(result.output)
    assert result.exit_code == 0
    assert result.output.strip() == credential['password']
