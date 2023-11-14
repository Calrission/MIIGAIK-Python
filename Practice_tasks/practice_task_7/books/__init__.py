import platform

slash = "/" if platform.system() == "Linux" else "\\"
path_to_books_csv = slash.join(__file__.split(slash)[0:-1] + ["books.csv"])

from .main import books, safe_input