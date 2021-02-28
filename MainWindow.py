import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5 import QtWidgets, uic
from SecondWindow import SecondWindow
from ThirdWindow import ThirdWindow
from FourthWindow import FourthWindow
from FifthWindow import FifthWindow
from SetLogic import SetLogic
from utils import show_message, to_set


def print_variant():
    g = 1  # Номер групи
    n = 2  # Номер у списку групи
    m = "IO"
    output = "Ім'я: Бугайчук Сергій Володимирович\n" + \
             "Група: " + str(m) + "-" + ("0" if g < 10 else "") + str(g) + \
             "\nНомер у групі: " + str(n)
    if m == "IO":
        n += 2
    variant = (n + g % 60) % 30 + 1
    output += "\nВаріант: " + str(variant)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(output)
    msg.setWindowTitle("Інформація")
    msg.exec_()


class MainWindow(QtWidgets.QMainWindow):
    def open_window(self, window_number):
        def func():
            self.windows[window_number].show()

        return func

    def set_power(self, which):
        def func():
            self.logic.set_power(which, self.powers[which].value())
            self.synchronize()

        return func

    def set_universal(self, which):
        def func():
            if which == 0 and self.universal[0].value() > self.logic.get_universal(1):
                self.universal[0].setValue(self.logic.get_universal(0))
                show_message("Укажіть правильний діапазон значень!")
            if which == 1 and self.universal[1].value() < self.logic.get_universal(0):
                self.universal[1].setValue(self.logic.get_universal(1))
                show_message("Укажіть правильний діапазон значень!")
            self.logic.set_universal(which, self.universal[which].value())
            self.synchronize()

        return func

    def set_field(self, which):
        def func():
            self.logic.set_field(which, to_set(self.set_fields[which].text()))
            self.set_fields[which].clear()
            self.synchronize()

        return func

    def generate_random(self):
        self.logic.generate()
        self.synchronize()

    def synchronize(self):
        for i in range(3):
            self.windows[i].update_value()

    def save_files(self):
        for i in range(3):
            self.windows[i].save_file(False)
        show_message("Усі файли (вікна номер 2, 3, 4) були збережені", QMessageBox.Information)

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('MainWindowForm.ui', self)
        self.logic = SetLogic()
        self.setWindowTitle("Вікно 1")
        self.powers = [self.power_a, self.power_b, self.power_c]
        self.universal = [self.universal_from, self.universal_to]
        self.set_powers = [self.set_power_a, self.set_power_b, self.set_power_c]
        self.set_fields = [self.set_a, self.set_b, self.set_c]
        self.set_fields_ok = [self.set_a_ok, self.set_b_ok, self.set_c_ok]
        self.windows = [SecondWindow(self.logic), ThirdWindow(self.logic), FourthWindow(self.logic),
                        FifthWindow(self.logic)]
        self.window_buttons = [self.windowBtn2, self.windowBtn3, self.windowBtn4, self.windowBtn5]
        for i in range(len(self.window_buttons)):
            self.window_buttons[i].clicked.connect(self.open_window(i))
        for i in range(len(self.set_powers)):
            self.powers[i].valueChanged.connect(self.set_power(i))
            self.set_powers[i].clicked.connect(self.set_power(i))
        for i in range(len(self.universal)):
            self.universal[i].valueChanged.connect(self.set_universal(i))
        for i in range(len(self.set_fields_ok)):
            self.set_fields_ok[i].clicked.connect(self.set_field(i))
        self.information.triggered.connect(print_variant)
        self.save_all_files.triggered.connect(self.save_files)
        self.generate_sets.clicked.connect(self.generate_random)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    app.exec_()
