from Practice_tasks.practice_task_2.paradox.monty_hall_paradox.game_ai import TypeResult

"""
Класс анализатора статистических данных
"""


class Analyst:
    def __init__(self):
        self.winnable_change = 0
        self.winnable_not_change = 0
        self.losable_not_change = 0
        self.losable_change = 0

    def parse_result(self, result):
        match result:
            case TypeResult.LOSE_NOT_CHANGE:
                self.new_lose_not_change()
            case TypeResult.WIN_NOT_CHANGE:
                self.new_win_not_change()
            case TypeResult.LOSE_CHANGE:
                self.new_lose_change()
            case TypeResult.WIN_CHANGE:
                self.new_win_change()

    def new_lose_not_change(self):
        self.losable_not_change += 1

    def new_win_not_change(self):
        self.winnable_not_change += 1

    def new_lose_change(self):
        self.losable_change += 1

    def new_win_change(self):
        self.winnable_change += 1

    @property
    def sum(self):
        return (self.winnable_not_change + self.winnable_change
                + self.losable_not_change + self.losable_change)

    @property
    def sum_winnable(self):
        return self.winnable_not_change + self.winnable_change

    @property
    def sum_losable(self):
        return self.losable_not_change + self.losable_change

    @property
    def sum_change(self):
        return self.losable_change + self.winnable_change

    @property
    def sum_not_change(self):
        return self.losable_not_change + self.winnable_not_change

    def strategy_one(self):
        result = round(self.winnable_not_change / self.sum_winnable, 2)
        return f"{result} ≈ {int(result * 100)}%"

    def strategy_two(self):
        result = round(self.winnable_change / self.sum_winnable, 2)
        return f"{result} ≈ {int(result * 100)}%"

    def __str__(self):
        return (
            f"За {self.sum} партий произошло: \n"
            f"Побед - {self.sum_winnable}\n"
            f"Поражений - {self.sum_losable}\n"
            f"{"-" * 30}\n"
            f"После открытия двери ведущим: \n"
            f"Сменили и победили - {self.winnable_change}\n"
            f"Сменили и проиграли - {self.losable_change}\n"
            f"Не сменили и победили - {self.winnable_not_change}\n"
            f"Не сменили и проиграли - {self.losable_not_change}\n"
            f"{"-" * 30}\n"
            f"Всего сменили - {self.sum_change}\n"
            f"Всего не сменили - {self.sum_not_change}\n"
            f"{"-" * 30}\n"
            f"Вероятность победить: \n"
            f"Если не менять выбор: {self.strategy_one()}\n"
            f"Если менять выбор: {self.strategy_two()}\n"
        )
