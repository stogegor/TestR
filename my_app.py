# напиши здесь код основного приложения и первого экрана
from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
class Mainwin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        pass
    def initUI(self):
        pass
    def connects(self):
        pass
app = QApplication([])
main_win = Mainwin()
app.exec_()
    



