# напиши здесь код третьего экрана приложения
from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
class Mainwin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.result()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.work_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)
    def result(self):
        index = (4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
