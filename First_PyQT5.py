from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def button_clicked():
    print(label.setText("Label Clicked"))


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("First Window App")

    label = QtWidgets.QLabel(win)
    label.setText("Label")
    label.move(50, 50)
    button = QtWidgets.QPushButton(win)
    button.setText("Button 1")
    button.clicked.connect(button_clicked)

    win.show()
    sys.exit(app.exec_())


window()
