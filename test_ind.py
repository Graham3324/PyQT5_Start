from test1 import Ui_MainWindow

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc


class TestWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button1.clicked.connect(lambda: self.label_change("button"))
        self.ui.actionAbout.triggered.connect(lambda: self.label_change("About item"))
        self.ui.actionClose.triggered.connect(lambda: self.label_change("Close item"))
        self.ui.actionExit.triggered.connect(lambda: self.label_change("Exit item"))
        self.ui.actionFly.triggered.connect(lambda: self.label_change("Fly item"))
        self.ui.actionOpen.triggered.connect(lambda: self.label_change("Open item"))

    def label_change(self, text):

        self.ui.label1.setText("You clicked the " + text)


if __name__ == "__main__":
    app = qtw.QApplication([])

    tester = TestWindow()
    tester.show()

    app.exec_()
