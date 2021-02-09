from PyQt5.QtWidgets import QApplication, QMessageBox, QToolTip
from PyQt5 import QtWidgets
import MainWindowForm

def print_variant():
    G = 1   # Номер групи
    N = 2   # Номер у списку групи
    M = "IO"
    output = "Моя група: " + str(M) + "-" + ("0" if G < 10 else "") + str(G) +\
             "\nМій номер у групі: " + str(N)
    if M == "IO":
        N += 2
    variant = (N + G % 60) % 30 + 1
    output += "\nМій варіант: " + str(variant)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(output)
    msg.setWindowTitle("Інформація")
    msg.exec_()


def foo(spinBox):
    return lambda: print(spinBox.value())


class MainWindow(QtWidgets.QMainWindow, MainWindowForm.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.windowBtn2.clicked.connect(print_variant)
        self.windowBtn3.clicked.connect(print_variant)
        self.windowBtn4.clicked.connect(print_variant)
        self.windowBtn5.clicked.connect(print_variant)
        self.information.triggered.connect(print_variant)


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec_()
