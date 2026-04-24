

from typing import Annotated, Union

from pydantic import Field

from rift_cli.data.buildings.resources.mine import Mine



BUILDING_UNION = Annotated[
    Union[Mine],
    Field(discriminator="type")
]