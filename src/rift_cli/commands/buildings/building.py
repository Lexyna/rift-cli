from rift_cli.commands.buildings.status import status
from rift_cli.commands.buildings.list import list
from rift_cli.commands.buildings.build import build
from rift_cli.commands.buildings.destroy import destroy
import click

@click.group
def buildings() -> None:
    pass

buildings.add_command(list)
buildings.add_command(build)
buildings.add_command(destroy)
buildings.add_command(status)