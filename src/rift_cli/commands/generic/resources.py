
from curses import meta
from email.policy import default
from random import choice, random, randrange
import re
from time import sleep
from zoneinfo import reset_tzpath

import click
from rich import box
from rich.live import Live
from rich.table import Table

from rift_cli.data.buildings.resources import mine
from rift_cli.data.game.gamedata import GameData, game_ctx
from rift_cli.data.resources import Grade, Resource, ResourceType, print_resource
from rift_cli.display.console import console
from rift_cli.display.formatter import format_number, number_to_roman
from rift_cli.functions.generic.resource_utils import player_add_resource


@click.command
@click.option("--live", "-l", is_flag=True, default=False,
              help="Displays live resource values")
@game_ctx
def resources(game: GameData, live) -> None:
    
    if live:
        with Live(create_res_table(game), refresh_per_second=20) as live:
            #TODO: Add proper update claculation/handling
            for i in range(10000):
                sleep(0.05)
                live.update(create_res_table(game))

        return

    console.log(create_res_table(game))

    pass

def create_res_table(game: GameData) -> Table:
    res_table: Table = Table(box=box.ASCII)

    res_table.add_column()
    res_table.add_column(ResourceType.METAL.format(), justify="right")
    res_table.add_column(ResourceType.MINERAL.format(), justify="right")
    res_table.add_column(ResourceType.CRYSTAL.format(), justify="right")
    res_table.add_column(ResourceType.LIQUID.format(), justify="right")
    res_table.add_column(ResourceType.GAS.format(), justify="right")
    res_table.add_column(ResourceType.ORGANIC.format(), justify="right")

    add_resource_rows(res_table, Grade.IMPURE, game)
    add_resource_rows(res_table, Grade.CRUDE, game)
    add_resource_rows(res_table, Grade.COMMON, game)
    add_resource_rows(res_table, Grade.REFINED, game)
    add_resource_rows(res_table, Grade.PURE, game)
    add_resource_rows(res_table, Grade.PRISTINE, game)

    return res_table

def add_resource_rows(res_table: Table, grade: Grade, game: GameData) -> None:

    metals: list[Resource] = []
    minerals: list[Resource] = []
    crystals: list[Resource] = []
    liquids: list[Resource] = []
    gases: list[Resource] = []
    organics: list[Resource] = []

    for res in game.resources.values():
        if res.grade == grade:
            match(res.type):
                case ResourceType.METAL: metals.append(res)
                case ResourceType.MINERAL: minerals.append(res)
                case ResourceType.CRYSTAL: crystals.append(res)
                case ResourceType.LIQUID: liquids.append(res)
                case ResourceType.GAS: gases.append(res)
                case ResourceType.ORGANIC: organics.append(res)

    first: bool = True

    metal_str: str = ""
    for res in metals:
        if not first:
            metal_str += "\n"
        first = False
        metal_str += f"{format_number(res.amount)} ({number_to_roman(res.lv)})"

    first = True
    mineral_str: str = ""
    for res in minerals:
        if not first:
            mineral_str += "\n"
        first = False
        mineral_str += f"{format_number(res.amount)} ({number_to_roman(res.lv)})"

    first = True
    crystals_str: str = ""
    for res in crystals:
        if not first:
            crystals_str += "\n"
        first = False
        crystals_str += f"{format_number(res.amount)} ({number_to_roman(res.lv)})"

    first = True
    liquid_str: str = ""
    for res in liquids:
        if not first:
            liquid_str += "\n"
        first = False
        liquid_str += f"{format_number(res.amount)} ({number_to_roman(res.lv)})"

    first = True
    gas_str: str = ""
    for res in gases:
        if not first:
            gas_str += "\n"
        first = False
        gas_str += f"{format_number(res.amount)} ({number_to_roman(res.lv)})"
   
    first = True
    organic_str: str = ""
    for res in organics:
        if not first:
            organic_str += "\n"
        first = False
        organic_str += f"{format_number(res.amount)} ({number_to_roman(res.lv)})"

    if not metal_str: metal_str = "N/A"
    if not mineral_str: mineral_str = "N/A"
    if not crystals_str: crystals_str = "N/A"
    if not liquid_str: liquid_str = "N/A"
    if not gas_str: gas_str = "N/A"
    if not organic_str: organic_str = "N/A"

    res_table.add_row(
        grade.format(),
        f"[{grade.col}]" + metal_str,
        f"[{grade.col}]" + mineral_str,
        f"[{grade.col}]" + crystals_str,
        f"[{grade.col}]" + liquid_str,
        f"[{grade.col}]" + gas_str,
        f"[{grade.col}]" + organic_str
    )

    pass