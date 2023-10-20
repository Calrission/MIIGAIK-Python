from typing import Callable


class Map:
    def __init__(self, word: list[tuple[str, bool]], on_all: Callable[[], None] = None):
        self.__word = word
        self.__on_all = on_all

    @staticmethod
    def new_word(word: str):
        return Map(word=[(i, False) for i in word])

    @staticmethod
    def empty():
        return Map.new_word("")

    @property
    def is_all(self):
        return all([i[1] for i in self.__word])

    @staticmethod
    def __on_change(fun):
        def wrapper(self, *args, **kwargs):
            result = fun(self, *args, **kwargs)
            if self.is_all:
                self.__on_all()
            else:
                return result
        return wrapper

    def add_on_win(self, fun: Callable[[], None]):
        self.__on_all = fun
        return self

    @__on_change
    def open(self, item: str) -> bool:
        if len(item) > 1 and self.__chars().lower() == item.lower():
            self.__word = [(i[0], True) for i in self.__word]
            return True
        if item in self:
            self.__word = [i if i[0].lower() != item.lower() else (i[0], True) for i in self.__word]
            return True
        return False

    def __chars(self) -> str:
        return "".join([i[0] for i in self.__word])

    def __contains__(self, item: str):
        return item.lower() in [i[0].lower() for i in self.__word]

    def __str__(self):
        return "".join([i[0] if i[1] else "⬛" if i != " " else " " for i in self.__word])
