import click
from rift_cli.commands.buildings.building import buildings
from rift_cli.commands.generic.init import init
from rift_cli.commands.generic.status import status
from rift_cli.commands.planets.planets import planets

@click.group
def cli():
    pass

cli.add_command(init)
cli.add_command(status)
cli.add_command(planets)
cli.add_command(buildings)

if __name__ == '__main__':
    cli()