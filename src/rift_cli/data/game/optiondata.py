from dataclasses import dataclass

@dataclass
class OptionData:
    tickrate: int = 10
    paused: bool = False