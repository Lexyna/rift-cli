from rift_cli.functions.generic.generators import generate_id, generate_planet_name
from rift_cli.data.planetdata import PlanetData

def create_planet() -> PlanetData:
    data = PlanetData(generate_id(), generate_planet_name(), 3)
    return data

