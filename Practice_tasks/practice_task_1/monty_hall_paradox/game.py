from random import randrange, choice


class Door:

    def __init__(self, is_open: bool, is_winnable: bool):
        self.__is_opened, self.__is_winnable = is_open, is_winnable

    @staticmethod
    def losable(): return Door(False, False)

    @staticmethod
    def winnable(): return Door(False, True)

    def check_win(self) -> bool:
        return self.__is_winnable and self.__is_opened

    @property
    def is_winnable(self) -> bool:
        return self.__is_winnable

    def open(self):
        self.__is_opened = True

    def copy(self):
        return Door(self.__is_opened, self.__is_winnable)

    def __mul__(self, other: int) -> tuple:
        return tuple(self.copy() for _ in range(other))

    def __str__(self):
        return f"{"?" if not self.__is_opened else "X" if not self.__is_winnable else "🪙"}"


class Game:
    def __init__(self):
        self._doors: tuple[Door, Door, Door]

    def prepare(self):
        self._regenerate_doors()

    def start(self):
        index_chosen_door = self._choose_door()
        index_opened_door = self._open_random_losable_door(index_ignore_door=index_chosen_door)
        self._show_final_choose(index_chosen_door=index_chosen_door, index_opened_door=index_opened_door)
        index_chosen_door = self._choose_door()
        choose_door = self._doors[index_chosen_door]
        choose_door.open()
        if choose_door.check_win():
            self.win()
        else:
            self.lose()

    def win(self):
        self._open_all_doors()
        self._show()
        print("Вы угадали !")

    def lose(self):
        self._open_all_doors()
        self._show()
        print("Вы не угадали !")

    def _regenerate_doors(self):
        index_winnable = randrange(0, 3)
        doors = Door.losable() * 2
        self._doors = doors[:index_winnable] + (Door.winnable(),) + doors[index_winnable:]

    def _open_random_losable_door(self, index_ignore_door: int) -> int:
        indexes_losable_doors = [i for i, e in enumerate(self._doors) if i != index_ignore_door and not e.is_winnable]
        index_opened_door: int = choice(indexes_losable_doors)
        self._doors[index_opened_door].open()
        return index_opened_door

    def _open_all_doors(self):
        for door in self._doors:
            door.open()

    def _choose_door(self):
        self._show()
        return self._input() - 1

    def _input(self) -> int:
        return int(input("Выберите дверь: "))

    def _show_final_choose(self, index_chosen_door: int, index_opened_door: int):
        print(f"Вы выбрали дверь под номером - {index_chosen_door + 1}. "
              f"Ведущий открывает дверь под номером - {index_opened_door + 1}")

    def _show(self):
        print(f"{"\n".join(f"Дверь №{i + 1} - {e}" for i, e in enumerate(self._doors))}")


if __name__ == "__main__":
    __game = Game()
    while True:
        print(f"{"-" * 10}Новая игра{"-" * 10}")
        __game.prepare()
        __game.start()
