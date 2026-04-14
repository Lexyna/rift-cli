import click
from rift_cli.commands.generic.init import init
from rift_cli.commands.generic.status import status

@click.group
def cli():
    pass

cli.add_command(init)
cli.add_command(status)

if __name__ == '__main__':
    cli()