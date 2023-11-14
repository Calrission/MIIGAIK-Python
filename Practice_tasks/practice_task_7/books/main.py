from . import path_to_books_csv
import csv

with open(path_to_books_csv, mode="r") as f:
    reader = csv.reader(f, delimiter="|")
    books = [[cell for cell in row] for row in reader]


def safe_input(fun, text: str = "", value_error: str = "", other_error: str = ""):
    while True:
        try:
            user_input = fun(input(text))
            return user_input
        except ValueError:
            print(value_error)
        except Exception:
            print(other_error)
