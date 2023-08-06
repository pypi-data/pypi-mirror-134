from __future__ import annotations

from typing import Any, Union
from dataclasses import dataclass, field
import re

# A nomie habit tracker. Tracks anything whose value can be encapsulated in a numerical value.
@dataclass(frozen=True)
class Tracker:
    tag: str
    label: str
    id: str
    one_tap: bool = True
    color: str = "#000080"
    emoji: str = ""
    hidden: bool = False
    ignore_zeros: bool = False
    math: str = "mean"
    type: str = "tick"  # tick or range mostly
    uom: str = ""
    # TODO no idea what include does
    include: str = ""
    min: int = 0
    max: int = 0
    goal: int = 0
    default: int = 0
    score: Union[int, str] = 1  # score can be string ('custom') or int
    score_calc: list[dict[str, Any]] = field(default_factory=lambda: [])

    def __post_init__(self):
        # ensure save as int if not 'custom' scoring
        if re.match(r"^-?[0-9]+$", str(self.score)):
            object.__setattr__(self, "score", int(self.score))


@dataclass(frozen=True)
class Activity:
    tracker: Tracker
    value: int = 1


# A nomie note. Records any circumstance of 'something happened' through prose.
# These are undigested events, whose changed trackers are still encapsulated
# in the 'note' field as continuous text.
@dataclass(frozen=True)
class Event:
    id: str
    start: int
    end: int
    text: str
    activities: list[Activity] = field(default_factory=lambda: [])
    score: int = 0
    lat: float = 0.0
    lng: float = 0.0
    location: str = ""
    modified: bool = False
    offset: str = ""  # local timezone offset?
    source: str = "n5"  # nomie version


@dataclass(frozen=True)
class NomieImport:
    version: str
    trackers: list[Tracker]
    events: list[Event]
