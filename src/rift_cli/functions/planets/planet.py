from rift_cli.data.resources import Deposit, Grade, Resource, ResourceType
from rift_cli.functions.generic.generators import generate_id, generate_planet_name
from rift_cli.data.planetdata import PlanetData

def create_planet() -> PlanetData:
    data = PlanetData(generate_id(), generate_planet_name(), 3)

    metal_deposit = Deposit(Resource(amount=4000))
    crystal_deposit = Deposit(Resource(type=ResourceType.CRYSTAL, amount=2000))

    data.deposits.append(metal_deposit)
    data.deposits.append(crystal_deposit)
    return data

