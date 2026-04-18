from dataclasses import dataclass, field

@dataclass
class OptionData:
    tickrate: int = field(default=10, init=True)        # ticks per seconds recalculated at the next command evaluatio
    hard_limit: bool = field(default=False, init=True)  # if true, no more then $compound_tick_limit can be processed
    ticklimit: int = field(default=300, init=True)      # max ticks allowed to process passively
    paused: bool = field(default=False, init=True)      # if true, calculate compound ticks, but sets $last_update
