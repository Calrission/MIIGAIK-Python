from task_1 import get_books, safe_input


def get_totals(books: list) -> list[tuple[str, float]]:
    return [(book[0], int(book[3]) * float(book[4])) for book in books]


if __name__ == "__main__":
    input_sub_title = safe_input(str, "Введите название книги: ")
    books = get_books(input_sub_title)
    result = get_totals(books)
    print(result)
