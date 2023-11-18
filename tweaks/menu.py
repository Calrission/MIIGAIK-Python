from sys import exit
from typing import Callable

from .directory import show_current_directory, change_directory, get_files, change_format_file, get_file_path
from .converter import convert_docx_to_pdf, convert_pdf_to_docx


def item_menu_change_current_directory():
    inp_user = input_with_exit("Укажите корректный путь к рабочему каталогу")
    if inp_user is None:
        return
    change_directory(inp_user)


def item_menu_convert(inp: str, out: str, converter):
    files = get_files(inp)

    def fun(index_file: int):
        file_path = get_file_path(files[index_file])
        output_file = change_format_file(file_path, out)
        print("Ожидайте...")
        converter(file_path, output_file)
        print(f"Готово. Создан {output_file}")

    choose_file(fun, files)


def item_menu_compress_image():
    pass


def item_menu_delete_group_files():
    pass


def choose_file(fun, files: list[str]):
    files_menu = {file: fun for file in files}
    if len(files_menu) == 0:
        print("Файлов с расширением docx в рабочем каталоге не найдено")
        return

    show_menu(files_menu)
    func, index = safe_choose_item_menu(files_menu)
    func(index)


menu = {
    "Сменить рабочий каталог": item_menu_change_current_directory,
    "Преобразовать PDF в Docx": lambda: item_menu_convert("pdf", "docx", convert_pdf_to_docx),
    "Преобразовать Docx в PDF": lambda: item_menu_convert("docx", "pdf", convert_docx_to_pdf),
    "Произвести сжатие изображения": item_menu_compress_image,
    "Удалить группу файлов": item_menu_delete_group_files,
    "Выход": exit,
}


def show_main_menu():
    show_menu(menu)


def show_menu(local_menu: dict):
    print("-" * 15 + "МЕНЮ" + "-" * 15)
    show_current_directory()
    print("\n".join(f"{i}. {e}" for i, e in enumerate(local_menu)))


def choose():
    func_item_menu, _ = safe_choose_item_menu(menu)
    func_item_menu()


def safe_choose_item_menu(local_menu: dict[str, Callable[[], None]]) -> (Callable[[], None], int):
    while True:
        try:
            usr_input = input("Введите индекс пункта меню: ")
            if usr_input is None:
                return lambda: None, -1
            index_item_menu = int(usr_input)
            return local_menu[list(local_menu.keys())[index_item_menu]], index_item_menu
        except ValueError:
            print("Ошибка! Введите число")
        except KeyError:
            print(f"Ошибка! Введите индекс меню от 0 до {len(local_menu)} включительно")


def input_with_exit(text: str) -> str | None:
    usr_input = input(f"{text} (exit - для выхода): ")
    if usr_input == "exit":
        return None
    return usr_input
