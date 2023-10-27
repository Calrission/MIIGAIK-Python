from Practice_tasks.practice_task_2.paradox.birthday_paradox.models import Group


def birthday(count_groups: int, count_first: int, count_second: int) -> str:
    """
    Проверка парадокса Дней Рождения:
    Генерируем две группы с днями рождения и считаем вероятность наличия хотя бы одной пары
    одинаковых дней рождения в каждой группе.
    :return: Вероятности
    :param count_groups: Кол-во генерируемых групп для одного типа (с 60-ю и с 23-я)
    :param count_first: Кол-во людей в первой группе
    :param count_second: Кол-во людей во второй группе
    """
    groups_1 = Group.generate_groups(count_groups, count_first)
    groups_2 = Group.generate_groups(count_groups, count_second)
    return (f"Вероятность нахождения хоть одной пары с одинаковыми днями рождения: \n"
            f"У первой группы ({count_first} чел.) - {Group.get_probability_equal_birthday_in_groups(groups_1)}%\n"
            f"У первой группы ({count_second} чел.) - {Group.get_probability_equal_birthday_in_groups(groups_2)}%")


if __name__ == "__main__":
    birthday(1000, 60, 23)
