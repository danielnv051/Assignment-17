""" from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

app = QApplication([])
loader = QUiLoader()
my_win = loader.load("my_win.ui")
my_win.show()

app.exec_()
 """

from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

my_app = QApplication([])

loader = QUiLoader()
window = loader.load("my_win.ui")
window.show()

my_app.exec()
 