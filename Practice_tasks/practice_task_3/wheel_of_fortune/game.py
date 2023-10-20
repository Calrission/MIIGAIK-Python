import sys
from random import randrange
from typing import Callable

from Practice_tasks.practice_task_3.wheel_of_fortune.health import Health, HealthMode
from Practice_tasks.practice_task_3.wheel_of_fortune.map import Map
from Practice_tasks.practice_task_3.wheel_of_fortune.records import Records
from Practice_tasks.practice_task_3.wheel_of_fortune.repository import parse_words


class Round:
    def __init__(
            self, word: str, difficulty: HealthMode,
            on_lose: Callable[[], None] = None, on_win: Callable[[], None] = None
    ):
        self.__health = Health.from_mode(difficulty).add_on_lose(on_lose)
        self.__map = Map.new_word(word).add_on_win(on_win)

    def start(self):
        while True:
            print(f"{self.__map} | {self.__health}")
            user_input = input("Введите букву или слово целиком: ")
            result = self.__map.open(user_input)
            if result is None:
                break
            if result:
                print("Правильно")
            else:
                self.__health.lose_one()
                if self.__health.is_dead:
                    break
                print("Неправильно. Вы теряете одну жизнь")

    def is_over(self) -> bool:
        return self.__map.is_all


class Game:
    def __init__(self):
        self.__records = Records()
        self.record = 0
        self.available_words = []
        self.select_mode: HealthMode = HealthMode.EASY

    def __choose_difficulty(self) -> HealthMode:
        while True:
            try:
                variant_index = int(input(f"{HealthMode.variants_str()}\nВыберите сложность (введите номер): ")) - 1
                return HealthMode.variants()[variant_index]
            except (ValueError, IndexError):
                print("Повторите повторно")

    def __change_difficulty(self):
        self.select_mode = self.__choose_difficulty()

    def __on_win(self):
        self.record += 1
        print("Вы победили")

    def save_record(self):
        user_name = input(f"Ваш счет: {self.record}\n"
                          f"Введите ваше имя для сохранения (введите skip чтобы не сохранять результат): ")
        if user_name == "skip":
            return
        self.__records.add_new_record(user_name, self.record)

    def __play(self):
        self.available_words = parse_words()
        self.record = 0
        while True:
            new_word = self.__pop_random_word()
            new_round = Round(
                new_word,
                self.select_mode,
                on_win=self.__on_win,
                on_lose=lambda: print(f"Вы проиграли, правильный ответ - {new_word}")
            )
            new_round.start()
            if self.__is_end():
                print("Вы сыграли все слова!")
                self.save_record()
                return
            print(f"Ваш счет: {self.record}")
            continue_game = self.__show_menu(
                menu={
                    "Продолжить": lambda: True,
                    "Выйти в меню": lambda: False,
                    "Выйти из игры": sys.exit
                }
            )()
            if not continue_game:
                self.save_record()
                break

    def __show_menu(
            self,
            menu: dict[str: Callable],
            input_text="Введите номер пункта меню: ",
            repeat_text="Повторите повторно"
    ) -> Callable:
        while True:
            print("\n".join([f"{i + 1}. {e}" for i, e in enumerate(menu.keys())]))
            try:
                index_menu_item = int(input(input_text)) - 1
                return menu[list(menu.keys())[index_menu_item]]
            except (ValueError, IndexError):
                print(repeat_text)

    def start(self):
        while True:
            print(f"Выбрана сложность {self.select_mode}")
            self.__show_menu(
                menu={
                    "Играть": self.__play,
                    "Изменить сложность": self.__change_difficulty,
                    "Таблица лидеров": lambda: print(self.__records),
                    "Выход": sys.exit
                }
            )()

    def __pop_random_word(self) -> str:
        index = randrange(0, len(self.available_words))
        word = self.available_words.pop(index)
        return word

    def __is_end(self):
        return len(self.available_words) == 0


if __name__ == "__main__":
    game = Game()
    game.start()
