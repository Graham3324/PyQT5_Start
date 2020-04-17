from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("First Window App")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Label")
        self.label.move(50, 50)
        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Button 1")
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.label.setText("Label Clicked")
        self.update()

    def update(self):
        self.label.adjustSize


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()
