from os import path
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from SetLogic import SetLogic
from utils import show_message, to_set, set_to_str


class FifthWindow(QMainWindow):
    def __init__(self, logic: SetLogic):
        super(FifthWindow, self).__init__()
        uic.loadUi('FifthWindowForm.ui', self)
        self.setWindowTitle("Вікно 5")
        self.logic = logic
        self.fields = [self.set_second, self.set_third, self.set_fourth, self.set_fifth]
        self.load_from_file.clicked.connect(self.load_files)

    def load_files(self):
        file_names = ["logs/data_second.txt", "logs/data_third.txt", "logs/data_fourth.txt"]
        for file_name in file_names:
            if not path.exists(file_name):
                show_message("File " + file_name + " does not exits")
                return
        files = [open(file_name, "r") for file_name in file_names]
        info = []
        for i in range(len(files)):
            t = files[i].read()
            info.append(to_set(t))
            self.fields[i].setText(t)
            files[i].close()
        self.fields[3].setText(set_to_str(self.logic.get_z_python()))
        info.append(self.logic.get_z_python())
        if info[0] == info[1] and info[2] == info[3]:
            self.is_match.setText("так")
        else:
            self.is_match.setText("ні")
