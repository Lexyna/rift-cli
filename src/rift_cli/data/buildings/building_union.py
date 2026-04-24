

from typing import Annotated, Union

from pydantic import Field

from rift_cli.data.buildings.resources.crystal.crystal_mine import CrystalMine
from rift_cli.data.buildings.resources.metal.metal_mine import MetalMine


BUILDING_UNION = Annotated[
    Union[MetalMine, CrystalMine],
    Field(discriminator="type")
]