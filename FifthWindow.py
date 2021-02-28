from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class FifthWindow(QMainWindow):
    def __init__(self):
        super(FifthWindow, self).__init__()
        uic.loadUi('FifthWindowForm.ui', self)
        self.setWindowTitle("Вікно 5")
