from rich.text import Text

from rift_cli.display.formatter import format_number
from rift_cli.utils.colors import color
from dataclasses import dataclass
from enum import Enum

class ResourceType(Enum):
    METAL = "metal"
    CREDITS = "credits"

@dataclass
class Deposit:
    type: ResourceType
    amount: int

def print_resource(type: ResourceType, value: int) -> str:
    
    txt_color = ""

    match type:
        case ResourceType.METAL: txt_color = f"{color.black}"
        case ResourceType.CREDITS: txt_color = f"{color.cyan}"
        case _: txt_color = f"{color.white}" 

    return Text(f"{type.name}: {format_number(value)}", f"{txt_color}")
