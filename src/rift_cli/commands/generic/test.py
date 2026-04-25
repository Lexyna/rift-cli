

from time import sleep

import click
from rich import live
from rich.live import Live
from rich.text import Text


@click.command
def test() -> None:
    
    val: int = 0

    with Live(make_text(val), refresh_per_second=10) as live:
        for i in range(100000):
            sleep(0.05)
            val += 1
            live.update(make_text(val))

    pass

def make_text(val: int) -> Text:
    return Text(f"Value: {val}")
