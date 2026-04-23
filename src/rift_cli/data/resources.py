from rich.text import Text

from rift_cli.display.formatter import format_number, number_to_roman
from rift_cli.utils.colors import color
from dataclasses import dataclass, field
from enum import Enum

class Grade(Enum):
    IMPURE = "Impure"
    CRUDE = "Crude"
    COMMON = "Common"
    REFINED = "Refined"
    PURE = "Pure"
    PRISTINE = "Pristine"

class ResourceType(Enum):
    METAL = "Metal"
    MINERAL = "Mineral"
    CRYSTAL = "Crystal"
    LIQUID = "Liquid"
    ORGANIC = "Organic"
    GAS = "Gas"

@dataclass
class Resource:
    grade: Grade = Grade.IMPURE
    type: ResourceType = ResourceType.METAL
    amount: int = 0
    lv: int = 1

@dataclass
class Deposit:
    resource: Resource = field(default_factory=Resource())
    extraction_diff: int = 1

def print_resource(res: Resource) -> str:
    
    txt_color = ""

    match res.type:
        case ResourceType.METAL: txt_color = f"{color.black}"
        case ResourceType.CRYSTAL: txt_color = f"{color.cyan}"
        case ResourceType.MINERAL: txt_color = f"{color.magenta}"
        case ResourceType.LIQUID: txt_color = f"{color.blue}"
        case ResourceType.ORGANIC: txt_color = f"{color.orange}"
        case ResourceType.GAS: txt_color = f"{color.yellow}"
        case _: txt_color = f"{color.white}" 

    return Text(f"{res.grade.name} {res.type.name}({number_to_roman(res.lv)}): {format_number(res.amount)}", f"{txt_color}")


def resource_to_key(res: Resource) -> str:
    return f"{res.grade.name}{res.type.name}({res.lv})"