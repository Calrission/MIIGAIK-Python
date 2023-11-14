from books import books, safe_input
import re


def get_books(sub_title: str) -> list[str]:
    pattern = fr"^(.*?(\b{sub_title}\b)[^$]*)$"
    return [book for i, book in enumerate(books) if i != 0 and re.match(pattern, book[1].lower())]


if __name__ == "__main__":
    input_sub_title = safe_input(str, "Введите название книги (чувствителен к регистру): ")
    books = get_books(input_sub_title)
    print(books)
