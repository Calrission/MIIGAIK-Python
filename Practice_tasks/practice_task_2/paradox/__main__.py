import sys

from Practice_tasks.practice_task_2.paradox import birthday, monty_hall

runs = {
    1: lambda: print(monty_hall(int(input("Введите кол-во итераций: ")))),
    2: lambda: print(birthday(int(input("Введите кол-во итераций: ")))),
    3: sys.exit
}

while True:
    user_input = int(input("Выберите парадокс:\n"
                           "1) Монти Холла\n"
                           "2) Дней рождения\n"
                           "3) Выход\n"
                           "Введите номер парадокса: "))
    runs[int(user_input)]()