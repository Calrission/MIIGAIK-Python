from Practice_tasks.practice_task_2.paradox.birthday_paradox.models import Group


def birthday(count_groups: int):
    """
    Проверка парадокса:
    Генерируем 1000 групп с 23-мя днями рождения и считаем вероятность наличия хотя бы одной пары
    одинаковых дней рождения.
    Повторяем для групп с 60-ю днями рождения.
    Вероятности выводим в консоль.
    :param count_groups: Кол-во генерируемых групп для одного типа (с 60-ю и с 23-я)
    """
    groups_23 = Group.generate_groups(count_groups, 23)
    groups_60 = Group.generate_groups(count_groups, 60)
    return (f"Вероятность нахождения хоть одной пары с одинаковыми днями рождения: \n"
            f"У групп с 23-мя днями - {Group.get_probability_equal_birthday_in_groups(groups_23)}%\n"
            f"У групп с 60-ю днями - {Group.get_probability_equal_birthday_in_groups(groups_60)}%")


if __name__ == "__main__":
    birthday(1000)
