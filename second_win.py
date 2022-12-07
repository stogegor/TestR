# напиши здесь код для второго экрана приложения
from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit

class Second_win(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_hello)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    #интерфейс
    def initUI(self):
        #кнопки
        self.btn_test1=QPushButton(txt_starttest1)
        self.btn_test2=QPushButton(txt_starttest2)
        self.btn_test3=QPushButton(txt_starttest3)
        self.btn_nextscr=QPushButton(txt_sendresults)
        #надписи
        self.name=QLabel(txt_name)
        self.age=QLabel(txt_age)
        self.test1=QLabel(txt_test1)
        self.test2=QLabel(txt_test2)
        self.test3=QLabel(txt_test3)
        self.time=QLabel('00:00')
        #поле ввода
        self.name_line=QLineEdit(txt_hintname)
        self.age_line=QLineEdit(txt_hintage)
        self.test1_line=QLineEdit(txt_hinttest1)
        self.test2_line=QLineEdit(txt_hinttest2)
        self.test3_line=QLineEdit(txt_hinttest3)
        #расположение
        self.layoutL=QVBoxLayout()
        self.layoutR=QVBoxLayout()
        self.main_layout=QHBoxLayout()
        #левая сторона
        self.layoutL.addWidget(self.name)
        self.layoutL.addWidget(self.name_line)
        self.layoutL.addWidget(self.age)
        self.layoutL.addWidget(self.age_line)
        self.layoutL.addWidget(self.test1)
        self.layoutL.addWidget(self.btn_test1)
        self.layoutL.addWidget(self.test1_line)
        self.layoutL.addWidget(self.test2)
        self.layoutL.addWidget(self.btn_test2)       
        self.layoutL.addWidget(self.test3)
        self.layoutL.addWidget(self.btn_test3)
        self.layoutL.addWidget(self.test2_line)
        self.layoutL.addWidget(self.test3_line)
        self.layoutL.addWidget(self.btn_nextscr)
        #правая сторона
        self.layoutR.addWidget(self.time)
        #расположение 2 сторон по горизонтали
        self.main_layout.addLayout(self.layoutL)
        self.main_layout.addLayout(self.layoutR)
        self.setLayout(self.main_layout)

    def connects(self):
        pass
    def next_click(self):
        pass

app=QApplication([])
screen2=Second_win()
app.exec_()

