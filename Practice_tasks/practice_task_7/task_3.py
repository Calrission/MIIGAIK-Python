import task_2
from task_2 import safe_input, get_books


def get_totals(books: list, limit: int = 500, add: int = 100) -> list[tuple[str, float]]:
    data = task_2.get_totals(books)
    return [i if i[1] >= limit else (i[0], i[1] + add) for i in data]


if __name__ == "__main__":
    input_sub_title = safe_input(str, "Введите название книги: ")
    input_limit = safe_input(int, "Введите лимит: ", "Введите число")
    input_add = safe_input(int, "Введите сумму добавление: ", "Введите число")
    books = get_books(input_sub_title)
    result = get_totals(books, limit=input_limit, add=input_add)
    print(result)
