from analyst import Analyst
from game_ai import GameAI


def start():
    """
    Функция запуска симуляции для проверки парадокса.
    Результат n-го кол-ва само-игр компьютера заносится в анализатор.
    В конце симуляции анализатор выводит статистику в консоль, где прописаны вероятности побед при разных стратегиях.
    """
    analyst = Analyst()
    game = GameAI()

    for _ in range(10000):
        game.prepare()
        game.start()
        result = game.result()
        analyst.parse_result(result)

    print(analyst)


if __name__ == "__main__":
    start()
