import os
from PyQt5.QtWidgets import QMessageBox


def show_message(text: str, message_type=QMessageBox.Warning):
    msg = QMessageBox()
    msg.setIcon(message_type)
    msg.setText(text)
    msg.setWindowTitle("Увага!")
    msg.exec_()


def set_to_str(to_convert: set):
    if len(to_convert) == 0:
        return "{}"
    else:
        return str(to_convert)


def can_convert(text: str):
    try:
        int(text)
        return True
    except ValueError:
        return False


def to_set(text: str):
    t = text.replace("{", "").replace("}", "").replace(",", " ")
    t = ' '.join(t.split())
    res = set()
    for i in t.split():
        if not can_convert(i):
            show_message("Перевірте правильність вводу множини!")
            return set()
        res.add(int(i))
    return res


def create_folder():
    if not os.path.exists("logs/"):
        os.mkdir("logs")
