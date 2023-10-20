import os

def parse_words() -> list[str]:
    path = "\\".join(__file__.split("\\")[:-1] + ["words.txt"])
    with open(path, mode="r", encoding="utf-8") as file:
        return file.read().split("\n")
