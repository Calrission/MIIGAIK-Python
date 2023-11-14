import pymorphy3
import csv
from translate import Translator


with open("dialogs.txt", mode="r") as file:
    words = file.read().split("\n")

morph = pymorphy3.MorphAnalyzer()
words = [morph.parse(word)[0].normal_form for word in words]

words_counts = {word: words.count(word) for word in set(words)}
words_counts = {key: words_counts[key] for key in sorted(words_counts, key=lambda x: words_counts[x], reverse=True)}

translator = Translator(from_lang="ru", to_lang="en")

with open("translated.txt", mode="w") as file:
    writer = csv.writer(file, delimiter="|")
    writer.writerow("Исходное слово | Перевод | Количество упоминаний".split(" | "))
    for index, pair in enumerate(words_counts.items()):
        word, count = pair
        translated_word = translator.translate(word)
        writer.writerow([word, translated_word.lower(), count])
        print(f"Переведено {index + 1}/{len(words_counts)}")


