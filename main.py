import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6 import uic


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("newwin.ui", self)


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()
