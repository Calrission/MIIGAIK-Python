from Practice_tasks.practice_task_6.models import *


def read_file(file_name: str) -> list[str]:
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read().split("\n")


def write_file(file_name: str, data: list[str]):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write("\n".join(data))


def parse_lines(data: list[str]) -> list[LogItem]:
    return [LogItem.from_text(line) for line in data]


if __name__ == "__main__":
    input_file_name = input("Введите название файла журнала: ")
    if input_file_name == "":
        input_file_name = "logs.txt"

    output_file_name = input("Введите название файла для вывода: ")
    if output_file_name == "":
        output_file_name = "result.txt"

    lines = read_file(input_file_name)
    logs = parse_lines(lines)
    write_file(output_file_name, list(map(str, logs)))
