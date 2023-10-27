import sys

from Practice_tasks.practice_task_2.paradox import birthday, monty_hall


def input_with_default(text, default):
    origin_input = input(text)
    if origin_input == "":
        return default
    return origin_input


def run_birthday():
    iterations = int(input_with_default("Введите кол-во итераций: ", 1000))
    first_group = int(input_with_default("Введите кол-во людей в первой группе: ", 63))
    second_group = int(input_with_default("Введите кол-во людей во второй группе: ", 20))
    print("Начало генерации... Ожидайте...")
    return birthday(iterations, first_group, second_group)


runs = {
    1: lambda: print(monty_hall(int(input("Введите кол-во итераций: ")))),
    2: lambda: print(run_birthday()),
    3: sys.exit
}

while True:
    user_input = int(input("Выберите парадокс:\n"
                           "1) Монти Холла\n"
                           "2) Дней рождения\n"
                           "3) Выход\n"
                           "Введите номер парадокса: "))
    runs[int(user_input)]()
