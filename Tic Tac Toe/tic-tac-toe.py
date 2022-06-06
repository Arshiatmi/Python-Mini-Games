# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import random


class Ui_MainWindow(object):
    shape = "O"
    tarColor = "#00007f"
    fullPattern = [["#", "#", "#"],
                   ["#", "#", "#"],
                   ["#", "#", "#"]]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 577)
        MainWindow.setStyleSheet("background-color: rgb(34, 13, 9);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 170, 681, 21))
        self.line.setStyleSheet("color: rgb(255, 255, 255);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 360, 681, 21))
        self.line_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(4)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(210, 0, 20, 531))
        self.line_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(440, -10, 20, 541))
        self.line_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(470, 10, 201, 151))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.button3.setFont(font)
        self.button3.setStyleSheet("color: rgb(255, 0, 0);")
        self.button3.setText("")
        self.button3.setCheckable(False)
        self.button3.setFlat(True)
        self.button3.setObjectName("button3")
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(470, 200, 201, 151))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.button6.setFont(font)
        self.button6.setStyleSheet("color: rgb(255, 0, 0);")
        self.button6.setText("")
        self.button6.setCheckable(False)
        self.button6.setFlat(True)
        self.button6.setObjectName("button6")
        self.button9 = QtWidgets.QPushButton(self.centralwidget)
        self.button9.setGeometry(QtCore.QRect(470, 380, 201, 151))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.button9.setFont(font)
        self.button9.setStyleSheet("color: rgb(255, 0, 0);")
        self.button9.setText("")
        self.button9.setCheckable(False)
        self.button9.setFlat(True)
        self.button9.setObjectName("button9")
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(240, 0, 201, 151))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.button2.setFont(font)
        self.button2.setStyleSheet("color: rgb(255, 0, 0);")
        self.button2.setText("")
        self.button2.setCheckable(False)
        self.button2.setFlat(True)
        self.button2.setObjectName("button2")
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(230, 200, 201, 151))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.button5.setFont(font)
        self.button5.setStyleSheet("color: rgb(255, 0, 0);")
        self.button5.setText("")
        self.button5.setCheckable(False)
        self.button5.setFlat(True)
        self.button5.setObjectName("button5")
        self.button8 = QtWidgets.QPushButton(self.centralwidget)
        self.button8.setGeometry(QtCore.QRect(240, 380, 201, 151))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.button8.setFont(font)
        self.button8.setStyleSheet("color: rgb(255, 0, 0);")
        self.button8.setText("")
        self.button8.setCheckable(False)
        self.button8.setFlat(True)
        self.button8.setObjectName("button8")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(10, 0, 201, 151))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.button1.setFont(font)
        self.button1.setStyleSheet("color: rgb(255, 0, 0);")
        self.button1.setText("")
        self.button1.setCheckable(False)
        self.button1.setFlat(True)
        self.button1.setObjectName("button1")
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(0, 200, 201, 151))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.button4.setFont(font)
        self.button4.setStyleSheet("color: rgb(255, 0, 0);")
        self.button4.setText("")
        self.button4.setCheckable(False)
        self.button4.setFlat(True)
        self.button4.setObjectName("button4")
        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        self.button7.setGeometry(QtCore.QRect(0, 380, 201, 151))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.button7.setFont(font)
        self.button7.setStyleSheet("color: rgb(255, 0, 0);")
        self.button7.setText("")
        self.button7.setCheckable(False)
        self.button7.setFlat(True)
        self.button7.setObjectName("button7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.button1.clicked.connect(self.button1_clicked)
        self.button2.clicked.connect(self.button2_clicked)
        self.button3.clicked.connect(self.button3_clicked)
        self.button4.clicked.connect(self.button4_clicked)
        self.button5.clicked.connect(self.button5_clicked)
        self.button6.clicked.connect(self.button6_clicked)
        self.button7.clicked.connect(self.button7_clicked)
        self.button8.clicked.connect(self.button8_clicked)
        self.button9.clicked.connect(self.button9_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tic Tac Toe"))

    # def change_shape(self):
    #     if self.shape == "O":
    #         self.shape = "X"
    #         self.tarColor = "#ff0000"
    #     else:
    #         self.shape="O"
    #         self.tarColor = "#00007f"

    def row_win(self):
        if self.fullPattern[0][0] == self.fullPattern[0][1] and self.fullPattern[0][1] == self.fullPattern[0][2] and self.fullPattern[0][0] != "#":
            return self.fullPattern[0][0]
        if self.fullPattern[1][0] == self.fullPattern[1][1] and self.fullPattern[1][1] == self.fullPattern[1][2] and self.fullPattern[1][0] != "#":
            return self.fullPattern[1][0]
        if self.fullPattern[2][0] == self.fullPattern[2][1] and self.fullPattern[2][1] == self.fullPattern[2][2] and self.fullPattern[2][0] != "#":
            return self.fullPattern[2][0]
        return "#"

    def col_win(self):
        if self.fullPattern[0][0] == self.fullPattern[1][0] and self.fullPattern[1][0] == self.fullPattern[2][0] and self.fullPattern[0][0] != "#":
            return self.fullPattern[0][0]
        if self.fullPattern[0][1] == self.fullPattern[1][1] and self.fullPattern[1][1] == self.fullPattern[2][1] and self.fullPattern[0][1] != "#":
            return self.fullPattern[0][1]
        if self.fullPattern[0][2] == self.fullPattern[1][2] and self.fullPattern[1][2] == self.fullPattern[2][2] and self.fullPattern[0][2] != "#":
            return self.fullPattern[0][2]
        return "#"

    def prod_win(self):
        t1 = self.fullPattern[0][2]
        t1Ok = True
        t2 = self.fullPattern[0][0]
        t2Ok = True
        if t1 == "#" and t2 == "#":
            return "#"
        else:
            for i in range(3):
                for j in range(3):
                    if i == (2 - j):
                        if self.fullPattern[i][j] != t1:
                            t1Ok = False
                    if i == j:
                        if self.fullPattern[i][j] != t2:
                            t2Ok = False
            if t1Ok:
                return t1
            if t2Ok:
                return t2
        return "#"

    def reset(self):
        ls = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6,
              self.button7, self.button8, self.button9]
        for i in ls:
            i.setText("")
            i.setStyleSheet("")
        for i in range(3):
            for j in range(3):
                self.fullPattern[i][j] = "#"

    def finish_game(self, which):
        msg = QMessageBox()
        if which == "E":
            msg.setWindowIcon(QtGui.QIcon('./e.png'))
            msg.setText(f"Well Done ! X = O !!! Game Will Be Reset ...")
            msg.setWindowTitle(f"POT !")
            msg.exec_()
            self.reset()
        else:
            if which == "X":
                msg.setWindowIcon(QtGui.QIcon('./x.png'))
            else:
                msg.setWindowIcon(QtGui.QIcon('./o.jpg'))
            msg.setText(f"{which} Won The Game !!! Game Will Be Reset ...")
            msg.setWindowTitle(f"{which} Won !")
            msg.exec_()
            self.reset()

    def checker(self, decide=True):
        v1 = self.row_win()
        if v1 != "#":
            self.finish_game(v1)
        v2 = self.col_win()
        if v2 != "#":
            self.finish_game(v2)
        v3 = self.prod_win()
        if v3 != "#":
            self.finish_game(v3)
        fulled = True
        for i in range(3):
            for j in range(3):
                if self.fullPattern[i][j] == "#":
                    fulled = False
                    break
        if fulled:
            self.finish_game("E")
        if decide:
            self.decide()

    def get_button_name(self, x, y):
        data = [[self.button1, self.button2, self.button3],
                [self.button4, self.button5, self.button6],
                [self.button7, self.button8, self.button9]]
        return data[x][y]

    def fill(self, x, y):
        shape = "X"
        tarColor = "#ff0000"
        self.fullPattern[x][y] = shape
        btn = self.get_button_name(x, y)
        btn.setText(shape)
        btn.setStyleSheet(f"color: {tarColor}")
        self.checker(False)

    def have_empty(self):
        for i in self.fullPattern:
            if i.count("#") != 0:
                return True
        return False

    def can_win(self, which):
        shape = which
        for i in range(3):
            if self.fullPattern[i].count(shape) >= 2 and self.fullPattern[i].count("#") == 1:
                return i, self.fullPattern[i].index("#")
            counter = 0
            x, y = 0, 0
            for j in range(3):
                if self.fullPattern[j][i] == shape:
                    counter += 1
                else:
                    x = j
                    y = i
                if counter >= 2 and self.fullPattern[x][y] == "#":
                    return x, y
        counter = 0
        c2 = 0
        x1, y1 = 0, 0
        x2, y2 = 0, 0
        for i in range(3):
            for j in range(3):
                if i == j:
                    if self.fullPattern[i][j] == shape:
                        counter += 1
                    else:
                        x1 = i
                        y1 = j
                if i == (2 - j):
                    if self.fullPattern[i][j] == shape:
                        c2 += 1
                    else:
                        x2 = i
                        y2 = j
        if counter >= 2 and self.fullPattern[x1][y1] == "#":
            return x1, y1
        if c2 >= 2 and self.fullPattern[x2][y2] == "#":
            return x2, y2
        return -1, -1

    def decide(self):
        check = self.can_win("O")
        if check[0] == -1 and check[1] == -1:
            if self.have_empty():
                checks = self.can_win("X")
                if checks[0] != -1 and checks[1] != -1:
                    self.fill(checks[0], checks[1])
                    return
                x = random.randint(0, 2)
                y = random.randint(0, 2)
                while self.fullPattern[x][y] != "#":
                    x = random.randint(0, 2)
                    y = random.randint(0, 2)
                self.fill(x, y)
        else:
            checks = self.can_win("X")
            if checks[0] != -1 and checks[1] != -1:
                self.fill(checks[0], checks[1])
                return
            self.fill(check[0], check[1])

    def button1_clicked(self):
        txt = self.button1.text()
        if not txt:
            self.button1.setStyleSheet(f"color: {self.tarColor};")
            self.button1.setText(self.shape)
            self.fullPattern[0][0] = self.shape
            # self.change_shape()
            self.checker()

    def button2_clicked(self):
        txt = self.button2.text()
        if not txt:
            self.button2.setStyleSheet(f"color: {self.tarColor};")
            self.button2.setText(self.shape)
            self.fullPattern[0][1] = self.shape
            # self.change_shape()
            self.checker()

    def button3_clicked(self):
        txt = self.button3.text()
        if not txt:
            self.button3.setStyleSheet(f"color: {self.tarColor};")
            self.button3.setText(self.shape)
            self.fullPattern[0][2] = self.shape
            # self.change_shape()
            self.checker()

    def button4_clicked(self):
        txt = self.button4.text()
        if not txt:
            self.button4.setStyleSheet(f"color: {self.tarColor};")
            self.button4.setText(self.shape)
            self.fullPattern[1][0] = self.shape
            # self.change_shape()
            self.checker()

    def button5_clicked(self):
        txt = self.button5.text()
        if not txt:
            self.button5.setStyleSheet(f"color: {self.tarColor};")
            self.button5.setText(self.shape)
            self.fullPattern[1][1] = self.shape
            # self.change_shape()
            self.checker()

    def button6_clicked(self):
        txt = self.button6.text()
        if not txt:
            self.button6.setStyleSheet(f"color: {self.tarColor};")
            self.button6.setText(self.shape)
            self.fullPattern[1][2] = self.shape
            # self.change_shape()
            self.checker()

    def button7_clicked(self):
        txt = self.button7.text()
        if not txt:
            self.button7.setStyleSheet(f"color: {self.tarColor};")
            self.button7.setText(self.shape)
            self.fullPattern[2][0] = self.shape
            # self.change_shape()
            self.checker()

    def button8_clicked(self):
        txt = self.button8.text()
        if not txt:
            self.button8.setStyleSheet(f"color: {self.tarColor};")
            self.button8.setText(self.shape)
            self.fullPattern[2][1] = self.shape
            # self.change_shape()
            self.checker()

    def button9_clicked(self):
        txt = self.button9.text()
        if not txt:
            self.button9.setStyleSheet(f"color: {self.tarColor};")
            self.button9.setText(self.shape)
            self.fullPattern[2][2] = self.shape
            # self.change_shape()
            self.checker()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
