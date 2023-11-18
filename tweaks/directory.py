from os.path import isdir, isfile, exists
from os import listdir
from sys import platform

is_linux = platform == "linux"
slash_platform = "\\" if "win" in platform.lower() else "/"
current_directory = slash_platform.join(__file__.split(slash_platform)[:-1])


def show_current_directory():
    print(f"Текущий каталог: {current_directory}")


def is_dir(dir_path: str) -> bool:
    return isdir(dir_path)


def is_file(file_path: str) -> bool:
    return isfile(file_path)


def is_exist(path: str) -> bool:
    return exists(path)


def is_exist_format_file(file: str) -> bool:
    return file.rfind(".") != -1


def get_format_file(file: str) -> str:
    return file[file.rfind(".") + 1:]


def remove_format(file: str) -> str:
    return file[:file.rfind(".")]


def change_format_file(file: str, new_format: str) -> str:
    return file[:file.rfind(".") + 1] + new_format


def append_postfix_filename(file: str, postfix: str) -> str:
    parts = file.split(slash_platform)
    filename = parts[-1]
    filename = filename[:filename.rfind(".")] + postfix + filename[filename.rfind("."):]
    return slash_platform.join(parts[:-1] + [filename])


def get_file_path(filename: str):
    return f"{current_directory}{slash_platform}{filename}"


def get_files(format_file: list) -> list[str]:
    files = listdir(current_directory)
    return [
        file for file in files
        if is_valid_file(f"{current_directory}{slash_platform}{file}", format_file, False)
    ]


def is_valid_directory(directory_path: str) -> bool:
    if not is_exist(directory_path):
        print(f"Ошибка! Директория {directory_path} не найдена")
        return False
    if not is_dir(directory_path):
        print(f"Ошибка! Путь {directory_path} указывает не на директорию")
        return False
    return True


def is_valid_file(file_path: str, file_format: list, show_errors: bool = True) -> bool:
    def print_error(*errors):
        if show_errors:
            print(*errors)

    if not is_exist(file_path):
        print_error(f"Ошибка! Файл {file_path} не найдена")
        return False
    if not is_file(file_path):
        print_error(f"Ошибка! Путь {file_path} указывает не на файл")
        return False
    if len(file_format) != 0:
        if not is_exist_format_file(file_path):
            print_error(f"Файл {file_path} не имеет формата")
            return False
        if get_format_file(file_path) not in file_format:
            print_error(f"Файл {file_path} не имеет нужный формат {file_format}")
            return False
    return True


def change_directory(new_directory: str) -> bool:
    global current_directory
    if not is_valid_directory(new_directory):
        return False

    current_directory = new_directory
