from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class FourthWindow(QMainWindow):
    def __init__(self):
        super(FourthWindow, self).__init__()
        uic.loadUi('FourthWindowForm.ui', self)
        self.setWindowTitle("Вікно 4")
