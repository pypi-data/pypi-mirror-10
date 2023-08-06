from datetime import datetime, timedelta
from functools import partial
import json
import os
import sys
import shutil

from tinydb.queries import where
import click
import yaml

from . import completion, clipboard
from ._compat import *
from .credential import split_fullname, make_fullname
from .crypt import Cryptor
from .database import Database
from .importers import find_importer
from .utils import genpass, load_config, ensure_dependencies
from .table import Table


__version__ = "0.2.2"

USER_CONFIG_PATH = os.path.expanduser('~/.passpierc')
DEFAULT_CONFIG = {
    'path': os.path.expanduser('~/.passpie'),
    'short_commands': False,
    'genpass_length': 32,
    'genpass_symbols': "_-#|+=",
    'table_format': 'fancy_grid',
    'headers': ['name', 'login', 'password', 'comment'],
    'colors': {'name': 'yellow', 'login': 'green'},
}
config = load_config(DEFAULT_CONFIG, USER_CONFIG_PATH)
genpass = partial(genpass,
                  length=config.genpass_length,
                  special=config.genpass_symbols)


class AliasedGroup(click.Group):

    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx)
                   if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        message = 'Too many matches: %s' % ', '.join(
            sorted([click.style(m, fg='yellow') for m in matches])
        )
        ctx.fail(message)


def get_credential_or_abort(db, fullname, many=False):
    try:
        login, name = split_fullname(fullname)
        query = (where("name") == name) & (where("login") == login)
    except ValueError:
        query = where('name') == fullname

    found = db.search(query) if many else db.get(query)
    if not found:
        message = "Credential '{}' not found".format(fullname)
        raise click.ClickException(click.style(message, fg='red'))
    elif db.count(query) > 1 and not many:
        message = "Multiple matches for '{}'".format(fullname)
        raise click.ClickException(click.style(message, fg='red'))

    return found


def ensure_is_database(path):
    try:
        assert os.path.isdir(path)
        assert os.path.isfile(os.path.join(path, '.keys'))
    except AssertionError:
        message = 'Not initialized database at {.path}'.format(config)
        raise click.ClickException(click.style(message, fg='yellow'))


def ensure_passphrase(db, passphrase):
    try:
        with Cryptor(db._storage.path) as cryptor:
            cryptor.check(passphrase, ensure=True)
        return passphrase
    except ValueError:
        message = 'Wrong passphrase'
        raise click.ClickException(click.style(message, fg='red'))


def print_table(credentials):
    from .table import Table

    if credentials:
        table = Table(
            config.headers,
            table_format=config.table_format,
            colors=config.colors,
            hidden=['password']
        )
        click.echo(table.render(credentials))


def copy_to_clipboard(text):
    try:
        clipboard.copy(text)
    except SystemError as exc:
        message = str(exc)
        raise click.ClickException(click.style(message, fg='red'))
    click.secho("Password copied to clipboard", fg="yellow")


@click.group(cls=AliasedGroup if config.short_commands else click.Group,
             invoke_without_command=True)
@click.option('-D', '--database', help='Alternative database path',
              type=click.Path(dir_okay=True, writable=True, resolve_path=True))
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx, database):
    try:
        ensure_dependencies()
    except RuntimeError as e:
        raise click.ClickException(click.style(str(e), fg='red'))

    if database:
        config.path = database

    if not ctx.invoked_subcommand == 'init':
        ensure_is_database(config.path)

    if ctx.invoked_subcommand is None:
        db = Database(config.path)
        credentials = sorted(db.all(), key=lambda x: x["name"]+x["login"])
        print_table(credentials)


@cli.command(help='completion script')
@click.argument('shell_name', type=click.Choice(completion.SHELLS))
@click.option('--commands', default=None)
def complete(shell_name, commands):
    commands = ['add', 'copy', 'remove', 'update']
    script = completion.script(shell_name, config.path, commands)
    click.echo(script)


@cli.command(help="Initialize new passpie database")
@click.option('--passphrase', prompt=True, hide_input=True,
              confirmation_prompt=True)
@click.option('--force', is_flag=True, help="force overwrite database")
def init(passphrase, force):
    if force and os.path.isdir(config.path):
        shutil.rmtree(config.path)

    try:
        with Cryptor(config.path) as cryptor:
            cryptor.create_keys(passphrase)
    except FileExistsError:
        message = "Database exists in {}. `--force` to overwrite".format(
            config.path)
        raise click.ClickException(click.style(message, fg='yellow'))
    click.echo("Initialized database in {}".format(config.path))


@cli.command(help="Add new credential")
@click.argument("fullname")
@click.option('-r', '--random', 'password', flag_value=genpass())
@click.password_option(help="Credential password")
@click.option('-c', '--comment', default="", help="Credential comment")
@click.option('-f', '--force', is_flag=True, help="Force overwriting")
@click.option('-C', '--copy', is_flag=True, help="Copy password to clipboard")
def add(fullname, password, comment, force, copy):
    db = Database(config.path)
    try:
        login, name = split_fullname(fullname)
    except ValueError:
        message = 'invalid fullname syntax'
        raise click.ClickException(click.style(message, fg='yellow'))

    found = db.get((where("login") == login) & (where("name") == name))
    if force or not found:
        with Cryptor(config.path) as cryptor:
            encrypted = cryptor.encrypt(password)

        credential = dict(fullname=fullname,
                          name=name,
                          login=login,
                          password=encrypted,
                          comment=comment,
                          modified=datetime.now())
        db.insert(credential)
        if copy:
            copy_to_clipboard(password)
    else:
        message = "Credential {} already exists. --force to overwrite".format(
            fullname)
        raise click.ClickException(click.style(message, fg='yellow'))


@cli.command(help="Update credential")
@click.argument("fullname")
@click.option("--name", help="Credential new name")
@click.option("--login", help="Credential new login")
@click.option("--comment", help="Credential new comment")
@click.option("--password", help="Credential new password")
@click.option('--random', 'password', flag_value=genpass(),
              help="Credential new randomly generated password")
def update(fullname, name, login, password, comment):
    db = Database(config.path)
    credential = get_credential_or_abort(db, fullname)
    values = credential.copy()

    if any([name, login, password, comment]):
        values["name"] = name if name else credential["name"]
        values["login"] = login if login else credential["login"]
        values["password"] = password if password else credential["password"]
        values["comment"] = comment if comment else credential["comment"]
    else:
        values["name"] = click.prompt("Name", default=credential["name"])
        values["login"] = click.prompt("Login", default=credential["login"])
        values["password"] = click.prompt("Password",
                                          hide_input=True,
                                          default=credential["password"],
                                          confirmation_prompt=True,
                                          show_default=False,
                                          prompt_suffix=" [*****]: ")
        values["comment"] = click.prompt("Comment",
                                         default=credential["comment"])

    if values != credential:
        values["fullname"] = make_fullname(values["login"], values["name"])
        values["modified"] = datetime.now()
        if values["password"] != credential["password"]:
            with Cryptor(config.path) as cryptor:
                values["password"] = cryptor.encrypt(values['password'])
        db = Database(config.path)
        db.update(values, (where("fullname") == credential["fullname"]))


@cli.command(help="Remove credential")
@click.argument("fullname")
@click.option("-y", "--yes", is_flag=True, help="Skip confirmation prompt")
def remove(fullname, yes):
    db = Database(config.path)
    credentials = get_credential_or_abort(db, fullname, many=True)

    if credentials:
        if not yes:
            creds = ', '.join([c['fullname'] for c in credentials])
            click.confirm(
                'Remove credentials: ({})'.format(
                    click.style(creds, 'yellow')),
                abort=True
            )
        for credential in credentials:
            db.remove(where('fullname') == credential['fullname'])


@cli.command(help="Copy credential password to clipboard/stdout")
@click.argument("fullname")
@click.option("--passphrase", prompt="Passphrase", hide_input=True)
@click.option("--to", default='clipboard', type=click.Choice(['stdout', 'clipboard']))
def copy(fullname, passphrase, to):
    db = Database(config.path)
    ensure_passphrase(db, passphrase)
    credential = get_credential_or_abort(db, fullname)

    with Cryptor(config.path) as cryptor:
        decrypted = cryptor.decrypt(credential["password"],
                                    passphrase=passphrase)
        if to == 'clipboard':
            copy_to_clipboard(decrypted)
        elif to == 'stdout':
            click.echo(decrypted)


@cli.command(help="Search credentials by regular expressions")
@click.argument("regex")
def search(regex):
    db = Database(config.path)
    credentials = db.search(
        where("name").matches(regex) |
        where("login").matches(regex) |
        where("comment").matches(regex))
    credentials = sorted(credentials, key=lambda x: x["name"]+x["login"])
    print_table(credentials)


@cli.command(help="Diagnose database for improvements")
@click.option("--full", is_flag=True, help="Show all entries")
@click.option("--days", default=90, type=int, help="Elapsed days")
@click.option("--passphrase", prompt="Passphrase", hide_input=True)
def status(full, days, passphrase):
    db = Database(config.path)
    ensure_passphrase(db, passphrase)
    credentials = sorted(db.all(), key=lambda x: x["name"]+x["login"])

    with Cryptor(config.path) as cryptor:
        for cred in credentials:
            cred["password"] = cryptor.decrypt(cred["password"], passphrase)

    if credentials:
        # check passwords
        for cred in credentials:
            repeated = [
                c["fullname"] for c in credentials
                if c["password"] == cred["password"] and c != cred
            ]
            if repeated:
                password = "Same as: {}".format(repeated)
                cred["repeated"] = click.style(password, "red")
            else:
                cred["repeated"] = click.style("OK", "green")

        for cred in credentials:
            cred['password'] = cred['repeated']

        # check modified time
        for cred in credentials:
            modified_delta = (datetime.now() - cred["modified"])
            if modified_delta > timedelta(days=days):
                modified_time = "{} days ago".format(modified_delta.days)
                cred["modified"] = click.style(modified_time, "red")

            else:
                cred["modified"] = click.style("OK", "green")

        if not full:
            credentials = [c for c in credentials
                           if c["password"] or c["modified"]]

        table = Table(["name", "login", "password", "modified"],
                      table_format=config.table_format)
        click.echo(table.render(credentials))


@cli.command(name="export", help="Export credentials in plain text")
@click.argument("dbfile", type=click.File("w"))
@click.option("--json", "as_json", is_flag=True, help="Export as JSON")
@click.option("--passphrase", prompt="Passphrase", hide_input=True)
def export_database(dbfile, as_json, passphrase):
    db = Database(config.path)
    ensure_passphrase(db, passphrase)
    credentials = db.all()

    with Cryptor(config.path) as cryptor:
        for cred in credentials:
            cred["password"] = cryptor.decrypt(cred["password"], passphrase)

    if as_json:
        for cred in credentials:
            cred["modified"] = str(cred["modified"])
        dict_content = {
            'handler': 'passpie',
            'version': 1.0,
            'credentials': [dict(x) for x in credentials],
        }
        content = json.dumps(dict_content, indent=2)
    else:
        dict_content = {
            'handler': 'passpie',
            'version': 1.0,
            'credentials': [dict(x) for x in credentials],
        }
        content = yaml.dump(dict_content, default_flow_style=False)

    dbfile.write(content)


@cli.command(name="import", help="Import credentials from path")
@click.argument("path", type=click.Path())
def import_database(path):
    importer = find_importer(path)
    if importer:
        credentials = importer.handle(path)
        db = Database(config.path)
        with Cryptor(config.path) as cryptor:
            for cred in credentials:
                encrypted = cryptor.encrypt(cred['password'])
                cred['password'] = encrypted
        db.insert_multiple(credentials)


@cli.command(help='Renew passpie database and re-encrypt credentials')
@click.option("--passphrase", prompt="Passphrase", hide_input=True)
def reset(passphrase):
    db = Database(config.path)
    ensure_passphrase(db, passphrase)
    new_passphrase = click.prompt('New passphrase',
                                  hide_input=True, confirmation_prompt=True)

    credentials = db.all()
    if credentials:
        with Cryptor(config.path) as cryptor:
            # decrypt passwords
            for cred in credentials:
                cred["password"] = cryptor.decrypt(cred["password"],
                                                   passphrase)

            # recreate keys
            cryptor.create_keys(new_passphrase, overwrite=True)

            # encrypt passwords
            for cred in credentials:
                cred["password"] = cryptor.encrypt(cred["password"])

        # remove old and insert re-encrypted credentials
        db.purge()
        db.insert_multiple(credentials)
