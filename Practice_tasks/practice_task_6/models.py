import dataclasses
from enum import Enum
from datetime import time, datetime


class TypeMovement(Enum):
    FROM = "из"
    TO = "в"

    @staticmethod
    def from_text(text: str):
        variants = [i for i in TypeMovement if i.value == text]
        if len(variants) == 0:
            return None
        return variants[0]

    def __str__(self):
        return self.value


@dataclasses.dataclass
class LogItem:
    number: int
    type_movement: TypeMovement
    city: str
    movement_time: time

    @staticmethod
    def from_text(text: str):
        parts = text.split(" ")
        return LogItem(
            number=int(parts[1]),
            type_movement=TypeMovement.from_text(parts[3]),
            city=parts[4],
            movement_time=datetime.strptime(parts[6], "%H:%M:%S").time()
        )

    def __str__(self):
        return f"[{self.movement_time.strftime("%H:%M:%S")}] - Поезд № {self.number} {self.type_movement} {self.city}"
