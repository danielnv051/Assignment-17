from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

my_app = QApplication([])
loader = QUiLoader()
my_window = loader.load("mainwindow.ui")
print(type(my_window))
