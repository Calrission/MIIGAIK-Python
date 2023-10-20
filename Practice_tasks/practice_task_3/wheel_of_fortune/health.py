from enum import Enum
from typing import Callable


class HealthMode(Enum):
    EASY = 7
    MEDIUM = 5
    HARD = 3

    @staticmethod
    def variants_str() -> str:
        return "\n".join([f"{i + 1}. {e}" for i, e in enumerate(HealthMode)])

    @staticmethod
    def variants() -> [str]:
        return [i for i in HealthMode]

    def __str__(self):
        return f"{self.name} - ❤x{self.value}"


class Health:
    def __init__(self, health: int = 0, on_lose: Callable[[], None] | None = None, mode=HealthMode.EASY):
        self.__health = health
        self.__on_lose = on_lose
        self.__mode = mode

    def restart(self):
        self.__health = self.__mode.value

    @property
    def health(self):
        return self.__health

    @property
    def is_dead(self):
        return self.__health == 0

    @staticmethod
    def __update_health(fun):
        def wrapper(self, *args, **kwargs):
            fun(self, *args, **kwargs)
            if self.__health < 0:
                self.__health = 0
            if self.check_lose():
                self.__on_lose()

        return wrapper

    @staticmethod
    def from_mode(mode: HealthMode):
        return Health(health=mode.value, mode=mode)

    def add_on_lose(self, fun: Callable[[], None]):
        self.__on_lose = fun
        return self

    @__update_health
    def lose_one(self):
        self.__health -= 1

    @__update_health
    def lose_many(self, count: int):
        self.__health -= min(count, self.__health)

    def check_lose(self) -> bool:
        return self.__health == 0

    def __str__(self):
        return f"❤x{self.__health}"
