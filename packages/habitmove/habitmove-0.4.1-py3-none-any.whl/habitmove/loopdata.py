from typing import Optional
from dataclasses import dataclass
from uuid import uuid4

# A loop Habit representation.
# Tracks anything whose value can be encapsulated in a numerical value.
@dataclass
class Habit:
    name: str
    type: int = 0  # 1 is range counter
    archived: int = 0
    color: int = 0
    highlight: int = 0
    freq_den: int = 1
    freq_num: int = 1
    target_value: int = 0
    description: str = ""
    question: str = ""
    unit: str = ""
    position: int = 0
    uuid: str = ""

    def __post_init__(self):
        if not self.uuid or self.uuid == "":
            self.uuid = uuid4().hex


# A Loop repetition representation, containing only the bare minimum
# for its successful entry into the Loop Habit Tracker database.
@dataclass
class Repetition:
    habit_uuid: str
    timestamp: int
    value: Optional[int]
