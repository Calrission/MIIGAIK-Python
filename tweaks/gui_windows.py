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
    window = sg.Window("Choose Quality", layout, size=(300, 200))
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



