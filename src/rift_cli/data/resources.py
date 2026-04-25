from rich.text import Text

from rift_cli.display.formatter import format_number, number_to_roman
from rift_cli.utils.colors import color
from dataclasses import dataclass, field
from enum import Enum

class PrintMixin:
    def format(self) -> str:
        return f"[{self.col}]{self.name}[/{self.col}]"

class Grade(PrintMixin, Enum):
    col: str
    grade: int
    def __new__(cls, value, color = "green", g = 0):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.col = color
        obj.grade = g
        return obj

    IMPURE = ("Impure", color.black, 0)
    CRUDE = ("Crude", color.yellow, 1)
    COMMON = ("Common", color.green, 2)
    REFINED = ("Refined", color.blue, 3)
    PURE = ("Pure", color.orange, 4)
    PRISTINE = ("Pristine", color.red, 5)

class ResourceType(PrintMixin, Enum):
    col: str
    def __new__(cls, value, color = "green"):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.col = color
        return obj
    
    METAL = ("Metal", color.black)
    MINERAL = ("Mineral", color.magenta)
    CRYSTAL = ("Crystal", color.cyan)
    LIQUID = ("Liquid", color.blue)
    ORGANIC = ("Organic", color.orange)
    GAS = ("Gas", color.yellow)

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
    return f"{res.grade.format()} {res.type.format()}({number_to_roman(res.lv)}): [{color.green}]{format_number(res.amount)}[/{color.green}]"


def resource_to_key(res: Resource) -> str:
    return f"{res.grade.name}{res.type.name}({res.lv})"