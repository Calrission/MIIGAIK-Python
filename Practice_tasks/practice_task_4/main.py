import string


def read_file(file_name: str) -> list[str]:
    with open(file_name, "r") as file:
        data = file.read().replace("\n", " ")
        for i in string.punctuation:
            data = data.replace(i, " ")
        return [i.lower() for i in data.split(" ")]


def save_file(file_name: str, words: list[str]):
    data = sorted(list(set(words)))
    with open(file_name, "w") as file:
        file.write(f"Всего уникальных слов: {len(data)}\n==============")
        file.write("\n".join(data))


if __name__ == "__main__":
    name_input = input("Введите название файла для ввода: ")
    if name_input == "":
        name_input = "data.txt"
    origin_words = read_file(name_input)
    name_output = input("Введите название файла для вывода: ")
    if name_output == "":
        name_output = "count.txt"
    save_file(name_output, origin_words)
    print(origin_words)
