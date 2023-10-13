from Practice_tasks.practice_task_2.paradox.monty_hall_paradox.analyst import Analyst
from Practice_tasks.practice_task_2.paradox.monty_hall_paradox.game_ai import GameAI


def monty_hall(n: int):
    """
    Функция запуска симуляции для проверки парадокса.
    Результат n-го кол-ва само-игр компьютера заносится в анализатор.
    В конце симуляции анализатор выводит статистику в консоль, где прописаны вероятности побед при разных стратегиях.
    """
    analyst = Analyst()
    game = GameAI()

    for _ in range(n):
        game.prepare()
        game.start()
        result = game.result()
        analyst.parse_result(result)

    return str(analyst)


if __name__ == "__main__":
    print(monty_hall(10000))
