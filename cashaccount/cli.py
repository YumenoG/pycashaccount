import click

from . import electron_markdown as ecmd
from . import opreturn as ophex
from . import KeyHashInfo, ScriptHashInfo
from . import Registration


@click.group()
def run():
    pass


@run.command()
@click.argument('name')
@click.argument('cash_or_legacy_address')
@click.option('--opreturn-hex', is_flag=True, default=False)
@click.option('--electron-markdown', is_flag=True, default=False)
def keyhash(name, cash_or_legacy_address, electron_markdown, opreturn_hex):
    try:
        info = KeyHashInfo(cash_or_legacy_address)
    except ValueError as e:
        raise click.exceptions.BadParameter(e)
    r = Registration(name, info)
    s = _format(r, electron_markdown, opreturn_hex)
    click.echo(s)


@run.command()
@click.argument('name')
@click.argument('cash_or_legacy_address', type=click.types.STRING)
@click.option('--opreturn-hex', is_flag=True, default=False)
@click.option('--electron-markdown', is_flag=True, default=False)
def scripthash(name, cash_or_legacy_address, electron_markdown, opreturn_hex):
    try:
        info = ScriptHashInfo(cash_or_legacy_address)
    except ValueError as e:
        raise click.exceptions.BadParameter(e)
    r = Registration(name, info)
    s = _format(r, electron_markdown, opreturn_hex)
    click.echo(s)


def _format(registration, electron_markdown, opreturn_hex):
    if electron_markdown:
        return ecmd(registration)
    elif opreturn_hex:
        return ophex(registration)
    return str(registration)
