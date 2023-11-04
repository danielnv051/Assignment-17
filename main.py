from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader


def test():
    print('salam salam')


my_app = QApplication([])
loader = QUiLoader()
my_window = loader.load("mainwindow.ui")
my_window.show()

my_window.pushButton.clicked.connect(test)

my_app.exec()
