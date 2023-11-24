import pymorphy3
import csv
from translate import Translator


def get_words() -> list[str]:
    with open("dialogs.txt", mode="r") as f:
        words = f.read().split("\n")
    return words


def to_normal(words: list[str]) -> list[str]:
    morph = pymorphy3.MorphAnalyzer()
    words = [morph.parse(word)[0].normal_form for word in words]
    return words


def to_dict(lst: list[str]) -> dict[str, int]:
    result = {word: lst.count(word) for word in set(lst)}
    result = {key: result[key] for key in sorted(result, key=lambda x: result[x], reverse=True)}
    return result


def translate_and_save(data: dict[str, int]):
    translator = Translator(from_lang="ru", to_lang="en")
    with open("translated.csv", mode="w") as file:
        writer = csv.writer(file, delimiter="|")
        writer.writerow("Исходное слово | Перевод | Количество упоминаний".split(" | "))
        for index, pair in enumerate(data.items()):
            word, count = pair
            translated_word = translator.translate(word)
            writer.writerow([word, translated_word.lower(), count])
            print(f"Переведено {index + 1}/{len(data)}")


if __name__ == "__main__":
    origin_words = get_words()
    normals_words = to_normal(origin_words)
    words_counts = to_dict(normals_words)
    translate_and_save(words_counts)
