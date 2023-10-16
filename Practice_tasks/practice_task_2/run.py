import sys

import paradox

runs = {
    1: lambda: print(paradox.monty_hall(int(input("Введите кол-во итераций: ")))),
    2: lambda: print(paradox.birthday(int(input("Введите кол-во итераций: ")))),
    3: sys.exit
}

while True:
    user_input = int(input("Выберите парадокс:\n"
                           "1) Монти Холла\n"
                           "2) Дней рождения\n"
                           "3) Выход\n"
                           "Введите номер парадокса: "))
    runs[int(user_input)]()
