from enum import Enum
from Practice_tasks.practice_task_2.paradox.monty_hall_paradox.game import Game, choice


class TypeResult(Enum):
    LOSE_NOT_CHANGE = 0
    LOSE_CHANGE = 1
    WIN_NOT_CHANGE = 2
    WIN_CHANGE = 3


class GameAI(Game):
    def __init__(self, show_log: bool = False):
        super().__init__()
        self.show_log = show_log
        self.__index_door_first_try = -1
        self.__index_door_second_try = -1
        self.__index_opened_door = -1
        self.is_win = False

    def _get_variables_input(self) -> list[int]:
        return [i + 1 for i, e in enumerate(self._doors) if i != self.__index_opened_door]

    def _open_random_losable_door(self, index_ignore_door: int) -> int:
        result = super()._open_random_losable_door(index_ignore_door)
        self.__index_opened_door = result
        return result

    def _input(self) -> int:
        variables = self._get_variables_input()
        index_door = choice(variables)
        if self.__index_door_first_try == -1:
            if self.show_log:
                print(f"Компьютер первый раз вводит '{index_door}'")
            self.__index_door_first_try = index_door
        else:
            if self.show_log:
                print(f"Компьютер второй раз вводит '{index_door}'")
            self.__index_door_second_try = index_door
        return index_door

    def _show_final_choose(self, index_chosen_door: int, index_opened_door: int):
        if self.show_log:
            print(f"Ведущий открывает дверь под номером - {index_opened_door + 1}")

    def result(self) -> TypeResult:
        assert self.__index_door_first_try != -1
        assert self.__index_door_second_try != -1
        is_change = self.__index_door_first_try != self.__index_door_second_try
        if self.is_win:
            if is_change:
                return TypeResult.WIN_CHANGE
            return TypeResult.WIN_NOT_CHANGE
        else:
            if is_change:
                return TypeResult.LOSE_CHANGE
            return TypeResult.LOSE_NOT_CHANGE

    def _show(self):
        if self.show_log:
            super()._show()

    def win(self):
        self.is_win = True
        self._open_all_doors()
        self._show()
        if self.show_log:
            print("Компьютер угадал")

    def lose(self):
        self._open_all_doors()
        self._show()
        if self.show_log:
            print("Компьютер не угадал")

    def prepare(self):
        super().prepare()
        self.is_win = False
        self.__index_door_first_try = -1
        self.__index_door_second_try = -1


if __name__ == "__main__":
    __game = GameAI(show_log=True)
    while True:
        print(f"{"-" * 10}Новая игра{"-" * 10}")
        input(f"Нажмите любую кнопку для следующей итерации")
        __game.prepare()
        __game.start()
