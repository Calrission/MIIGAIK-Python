from os import remove

import PySimpleGUI as sg

from tweaks.directory import *
from tweaks.error import MessageException


def show_change_directory_window() -> str | None:
    layout = [
        [sg.Text("Выберите новую рабочую директорию: ")],
        [sg.Input(default_text="Выберите папку", disabled=True), sg.FolderBrowse(key="PATH")],
        [sg.Button("Отмена"), sg.Button("Потвердеть")]
    ]
    window = sg.Window("Change Directory", layout)
    while True:
        event, values = window.read()
        if event == "Отмена" or event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == "Потвердеть":
            new_directory = values["PATH"]
            try:
                change_directory(new_directory)
                window.close()
                return new_directory
            except MessageException as e:
                sg.Popup(e.args[0], keep_on_top=True, title="Ошибка")


def show_choose_file(formats: list[str]) -> str | None:
    files = get_files(formats, do_raise=False)
    layout = [
        [
            sg.Column(
                [[sg.Button(file, key=f"CHOOSE {file}")] for file in files],
                scrollable=True, vertical_scroll_only=True, size=(200, 200)
            )
        ]
    ]
    window = sg.Window("Choose File", layout, size=(200, 200))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            return None
        elif "CHOOSE" in event:
            file = event.split(" ")[1]
            window.close()
            return get_file_path(file)


def show_set_quality_window() -> int | None:
    layout = [
        [sg.Text("Укажите качество сжатия изображения")],
        [sg.Slider(range=(0, 100), orientation="h", key="SLIDER", enable_events=True)],
        [sg.Button("Отменить"), sg.Button("Потвердеть")]
    ]
    window = sg.Window("Choose Quality", layout)
    value = 0
    while True:
        event, values = window.read()
        if event == "Отменить" or event == sg.WIN_CLOSED:
            window.close()
            return None
        elif event == "SLIDER":
            value = int(values["SLIDER"])
        elif event == "Потвердеть":
            window.close()
            return value


def show_input_substring() -> str | None:
    layout = [
        [sg.Text("Введите подстроку")],
        [sg.Input(key="SUBSTRING")],
        [sg.Button("Потвердеть")]
    ]
    window = sg.Window("Input substring", layout, size=(300, 100))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            return None
        elif event == "Потвердеть":
            substring = values["SUBSTRING"]
            if substring == "":
                sg.PopupOK("Введите подстроку")
            else:
                window.close()
                return substring


def show_input_format() -> str | None:
    layout = [
        [sg.Text("Введите расширение")],
        [sg.Input(key="SUBSTRING")],
        [sg.Button("Потвердеть")]
    ]
    window = sg.Window("Input substring", layout, size=(300, 100))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            return None
        elif event == "Потвердеть":
            substring = values["SUBSTRING"]
            if substring == "":
                sg.PopupOK("Введите подстроку")
            else:
                window.close()
                return substring


def show_delete_many_files_window():
    items = ["Удалить все файлы начинающиеся на определенную подстроку",
             "Удалить все файлы заканчивающиеся на определенную подстроку",
             "Удалить все файлы содержащиеся определенную подстроку",
             "Удалить все файлы по расширению"]
    layout = [
        [sg.Button(item)] for item in items
    ]
    window = sg.Window("Choose Category delete", layout, size=(500, 200))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            return
        elif event == items[0]:
            substring = show_input_substring()
            if substring is None:
                continue
            all_files = get_files([], do_raise=False)
            need_files = [get_file_path(file) for file in all_files if file.lower().startswith(substring.lower())]
            result = sg.PopupOKCancel(f"Будут удалены {len(need_files)} шт. файлов")
            if result == "OK":
                window.close()
                return need_files
            else:
                return None
        elif event == items[1]:
            substring = show_input_substring()
            if substring is None:
                continue
            all_files = get_files([], do_raise=False)
            need_files = [get_file_path(file) for file in all_files if file.lower().endswith(substring.lower())]
            result = sg.PopupOKCancel(f"Будут удалены {len(need_files)} шт. файлов")
            if result == "OK":
                window.close()
                return need_files
            else:
                return None
        elif event == items[2]:
            substring = show_input_substring()
            if substring is None:
                continue
            all_files = get_files([], do_raise=False)
            need_files = [get_file_path(file) for file in all_files if substring.lower() in file.lower()]
            result = sg.PopupOKCancel(f"Будут удалены {len(need_files)} шт. файлов")
            if result == "OK":
                window.close()
                return need_files
            else:
                return None
        elif event == items[3]:
            format_file = show_input_format()
            if format_file is None:
                continue
            need_files = get_files([format_file], do_raise=False)
            result = sg.PopupOKCancel(f"Будут удалены {len(need_files)} шт. файлов")
            if result == "OK":
                window.close()
                return need_files
            else:
                return None
