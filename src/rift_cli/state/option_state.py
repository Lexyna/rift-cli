from dataclasses import dataclass

@dataclass
class OptionState:
    tickrate: int = 10
    paused: bool = False