from copy import copy

from rift_cli.data.game.gamedata import GameData
from rift_cli.data.resources import Resource, resource_to_key


def player_add_resource(game: GameData, res: Resource, amount: int) -> None:
    key = resource_to_key(res)
    if not key in game.resources:
        game.resources[key] = copy(res)
        game.resources[key].amount = 0
    game.resources[key].amount += amount
    pass