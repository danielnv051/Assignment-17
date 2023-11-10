from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

app = QApplication([])
loader = QUiLoader()
my_win = loader.load("newwin.ui")
my_win.show()

app.exec()
