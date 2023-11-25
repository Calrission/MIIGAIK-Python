from .gui_windows import *
from .terminal_menu import menu
from .converter import *
from .compressor import *


def run_gui():
    menu_items = list(menu.keys())

    layout = [
        [[sg.Text("Текущая рабочая директория:\n" + current_directory, key="TEXT", size=(400, None))]],
        [[sg.Button(item)] for item in menu_items]
    ]
    window = sg.Window("Office Tweaks", layout, size=(400, 250))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Выход':
            break
        elif event == menu_items[0]:
            new_directory = show_change_directory_window()
            if new_directory is not None:
                window["TEXT"].update("Текущая рабочая директория:\n" + new_directory)
        elif event == menu_items[1]:
            choose_file = show_choose_file(["pdf"])
            if choose_file is not None:
                new_docx = change_format_file(choose_file, "docx")
                convert_pdf_to_docx(choose_file, new_docx)
                sg.Popup(f"Готово, файл создан {new_docx}")
        elif event == menu_items[2]:
            choose_file = show_choose_file(["docx"])
            if choose_file is not None:
                new_pdf = change_format_file(choose_file, "pdf")
                convert_docx_to_pdf(choose_file, new_pdf)
                sg.Popup(f"Готово, файл создан {new_pdf}")
        elif event == menu_items[3]:
            choose_file = show_choose_file(["png", "jpg", "jpeg"])
            if choose_file is not None:
                quality = show_set_quality_window()
                if quality is not None:
                    new_file = append_postfix_file(choose_file, "_compress")
                    compress(choose_file, new_file)
                    sg.Popup(f"Готово, файл создан {new_file}")


    window.close()
