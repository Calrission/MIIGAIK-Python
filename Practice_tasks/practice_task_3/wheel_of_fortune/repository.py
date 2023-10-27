from Practice_tasks.practice_task_3.wheel_of_fortune.utils import slash


def parse_words() -> list[str]:
    path = slash().join(__file__.split(slash())[:-1] + ["words.txt"])
    with open(path, mode="r", encoding="utf-8") as file:
        return file.read().split("\n")
