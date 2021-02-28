from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from SetLogic import SetLogic
from utils import set_to_str, show_message, create_folder


class FourthWindow(QMainWindow):
    def __init__(self, logic: SetLogic):
        super(FourthWindow, self).__init__()
        uic.loadUi('FourthWindowForm.ui', self)
        self.setWindowTitle("Вікно 4")
        self.logic = logic
        self.save_to_file.clicked.connect(self.save_file)

    def update_value(self):
        self.set_x.setText(set_to_str(self.logic.get_x()))
        self.set_y.setText(set_to_str(self.logic.get_y()))
        self.set_z.setText(set_to_str(self.logic.get_z()))

    def save_file(self, message_shown=True):
        create_folder()
        f = open("logs/data_fourth.txt", "w")
        f.write(str(self.logic.get_z()))
        if message_shown:
            show_message("Інформацію збережено до файлу logs/data_fourth.txt", QMessageBox.Information)
        f.close()

