from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from SetLogic import SetLogic
from utils import show_message, create_folder


class SecondWindow(QMainWindow):
    def __init__(self, logic: SetLogic):
        super(SecondWindow, self).__init__()
        uic.loadUi('SecondWindowForm.ui', self)
        self.setWindowTitle("Вікно 2")
        self.logic = logic
        self.fields = [self.set_a, self.set_b, self.set_c]
        self.long_steps = ["A ⋂ B", "A \\ B", "C ∪ B", "(A ⋂ B) ∪ (A \\ B)", "((A ⋂ B) ∪ (A \\ B)) Δ (С ∪ B)"]
        self.current_step = 0
        self.current_value = set()
        self.result_value = set()
        self.change_step(True, True)()
        self.next_step.clicked.connect(self.change_step(True, False))
        self.last_step.clicked.connect(self.change_step(False, False))
        self.save_to_file.clicked.connect(self.save_file)
        self.update_value()

    def save_file(self, message_shown=True):
        create_folder()
        f = open("logs/data_second.txt", "w")
        f.write(str(self.result_value))
        if message_shown:
            show_message("Інформацію збережено до файлу logs/data_second.txt", QMessageBox.Information)
        f.close()

    def change_step(self, is_next: bool, is_update: bool):
        def foo():
            if not is_update:
                if is_next:
                    if self.current_step + 1 >= len(self.long_steps):
                        show_message("Останній крок уже показується")
                        return
                    self.current_step += 1
                else:
                    if self.current_step == 0:
                        show_message("Ви знаходитесь на першому кроці")
                        return
                    self.current_step -= 1
            self.expression.setText(self.long_steps[self.current_step])
            self.set_d.setText(str(self.result_value))
            self.current_value = self.calculate_step()
            if len(self.result_value) == 0:
                self.set_d.setText("{}")
            else:
                self.set_d.setText(str(self.result_value))
            if len(self.current_value) == 0:
                self.result.setText("{}")
            else:
                self.result.setText(str(self.current_value))

        return foo

    def calculate_step(self):
        res = a = self.logic.fields[0]
        b = self.logic.fields[1]
        c = self.logic.fields[2]
        if self.current_step == 0:
            res = a & b
        elif self.current_step == 1:
            res = a - b
        elif self.current_step == 2:
            res = c | b
        elif self.current_step == 3:
            res = (a & b) | (a - b)
        elif self.current_step == 4:
            res = ((a & b) | (a - b)) ^ (c | b)
        self.result_value = ((a & b) | (a - b)) ^ (c | b)
        return res

    def update_value(self):
        for i in range(len(self.fields)):
            if len(self.logic.fields[i]) == 0:
                self.fields[i].setText("{}")
            else:
                self.fields[i].setText(str(self.logic.fields[i]))
        self.change_step(True, True)()
