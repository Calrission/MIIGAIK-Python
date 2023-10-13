from dataclasses import dataclass
from random import randint
from itertools import product


@dataclass
class Birthday:
    day: int
    month: int

    @staticmethod
    def random():
        """
        Сгенерировать день рождения (Birthday) со случайной датой
        :return: День рождения (Birthday)
        """
        return Birthday(
            day=randint(1, 28),
            month=randint(1, 12)
        )

    def __eq__(self, other) -> bool:
        return isinstance(other, Birthday) and other.day == self.day and other.month == self.month


@dataclass
class Pair:
    first: Birthday
    second: Birthday

    def equal(self) -> bool:
        """
        Равны ли два дня рождения (Birthday) пары (Pair)
        :return: Равны / не равны
        """
        return self.first == self.second

    @staticmethod
    def from_tuple(pair: tuple[Birthday, Birthday]):
        """
        Создание экземпляра пары (Pair) с помощью двух-элементного кортежа дней рождений (Birthday)
        :param pair: Двух-элементный кортеж дней рождений (Birthday)
        :return: Пара (Pair)
        """
        return Pair(
            first=pair[0],
            second=pair[1]
        )


@dataclass
class Group:
    birthdays: list[Birthday]

    @staticmethod
    def generate(count: int):
        """
        Генерация одной группы (Group) c определённым кол-вом дней рождений (Birthday)
        :param count: Кол-во дней рождений
        :return: Группа (Group)
        """
        return Group(
            birthdays=[Birthday.random() for _ in range(count)]
        )

    @staticmethod
    def generate_groups(count_groups: int, count_birthdays_one_group: int) -> list:
        """
        Массовая генерация групп
        :param count_groups: Кол-во групп (Group)
        :param count_birthdays_one_group: Кол-во дней рождений в одной группе
        :return: Список групп (Group)
        """
        return [Group.generate(count_birthdays_one_group) for _ in range(count_groups)]

    def exist_pair_with_equal_birthday(self) -> bool:
        """
        Существует ли в этой группе хотя бы одна пара (Pair) одинаковых дней рождений.
        :return: Существует / Не существует
        """
        pairs = self.get_pairs()
        for i in pairs:
            if i.equal():
                return True
        return False

    @staticmethod
    def get_probability_equal_birthday_in_groups(groups: list) -> float:
        """
        Получение вероятности нахождение в списке групп группы с хотя бы одной парой с одинаковыми днями рождения
        :param groups: Список групп (экземпляров класса Group)
        :return: Вероятность в процентах
        """
        return round(sum([1 for i in groups if i.exist_pair_with_equal_birthday()]) / len(groups) * 100, 2)

    def get_pairs(self) -> list[Pair]:
        """
        Получение всех возможных пар (Pair) дней рождения из группы
        :return: Список пар (Pair) дней рождений
        """
        return [Pair.from_tuple(i) for i in list(product(self.birthdays, self.birthdays)) if not (i[0] is i[1])]
