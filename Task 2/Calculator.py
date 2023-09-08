from PyQt5 import *
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, \
    QTextEdit, QLineEdit, QListWidget, QGridLayout
from PyQt5 import QtGui
from PyQt5 import QtCore


class Main_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ZEUS CALCULATOR")
        self.icon=QIcon('images/icons8-calculator-64.png')
        self.setWindowIcon(QIcon('images/icons8-calculator-64.png'))

        self.mainlayout = QVBoxLayout()
        self.mainlayout1 = QVBoxLayout()
        self.mainlayout2 = QGridLayout()

        self.screen = QLabel()
        self.screen.setMinimumHeight(80)
        self.screen.setMinimumWidth(430)
        self.screen.setMaximumHeight(80)
        self.screen.setMaximumWidth(430)
        self.screen.setWordWrap(True)
        self.screen.setStyleSheet("QLabel"
                                  "{"
                                  "border : 3px solid Black;"
                                  "background : white ; "
                                  "color : black ;"
                                  "}")
        self.screen.setAlignment(Qt.AlignLeft)
        self.screen.setFont(QFont('Arial', 18))
        self.mainlayout1.addWidget(self.screen)

        self.bC = QPushButton("C")
        self.bC.setFont(QFont('Arial', 14))
        self.bC.setFixedSize(100, 100)
        self.mainlayout2.addWidget(self.bC, 0, 0, QtCore.Qt.AlignCenter)
        self.bC.clicked.connect(lambda: self.calc(self.bC.text()))

        self.bBO = QPushButton("(")
        self.bBO.setFont(QFont('Arial', 14))
        self.bBO.setFixedSize(100, 100)
        self.mainlayout2.addWidget(self.bBO, 0, 1, QtCore.Qt.AlignCenter)
        self.bBO.clicked.connect(lambda: self.calc(self.bBO.text()))

        self.bBC = QPushButton(")")
        self.bBC.setFont(QFont('Arial', 14))
        self.bBC.setFixedSize(100, 100)
        self.mainlayout2.addWidget(self.bBC, 0, 2, QtCore.Qt.AlignCenter)
        self.bBC.clicked.connect(lambda: self.calc(self.bBC.text()))

        self.bBPP = QPushButton("%")
        self.bBPP.setFont(QFont('Arial', 14))
        self.bBPP.setFixedSize(100, 100)
        self.mainlayout2.addWidget(self.bBPP, 0, 3, QtCore.Qt.AlignCenter)
        self.bBPP.clicked.connect(lambda: self.calc(self.bBPP.text()))

        self.bB1 = QPushButton("1")
        self.bB1.setFont(QFont('Arial', 14))
        self.bB1.setFixedSize(100, 100)
        self.mainlayout2.addWidget(self.bB1, 1, 0, QtCore.Qt.AlignCenter)
        self.bB1.clicked.connect(lambda: self.calc(self.bB1.text()))

        self.bB2 = QPushButton("2")
        self.bB2.setFont(QFont('Arial', 14))
        self.bB2.setFixedSize(100, 100)
        self.mainlayout2.addWidget(self.bB2, 1, 1, QtCore.Qt.AlignCenter)
        self.bB2.clicked.connect(lambda: self.calc(self.bB2.text()))

        self.bB3 = QPushButton("3")
        self.bB3.setFont(QFont('Arial', 14))
        self.bB3.setFixedSize(100, 100)
        self.mainlayout2.addWidget(self.bB3, 1, 2, QtCore.Qt.AlignCenter)
        self.bB3.clicked.connect(lambda: self.calc(self.bB3.text()))

        self.bBP = QPushButton("+")
        self.bBP.setFont(QFont('Arial', 14))
        self.bBP.setFixedSize(100, 100)
        self.mainlayout2.addWidget(self.bBP, 1, 3, QtCore.Qt.AlignCenter)
        self.bBP.clicked.connect(lambda: self.calc(self.bBP.text()))

        self.bB4 = QPushButton("4")
        self.bB4.setFont(QFont('Arial', 14))
        self.bB4.setFixedSize(100, 100)
        self.mainlayout2.addWidget(self.bB4, 2, 0, QtCore.Qt.AlignCenter)
        self.bB4.clicked.connect(lambda: self.calc(self.bB4.text()))

        self.bB5 = QPushButton("5")
        self.bB5.setFont(QFont('Arial', 14))
        self.bB5.setFixedSize(100, 100)
        self.mainlayout2.addWidget(self.bB5, 2, 1, QtCore.Qt.AlignCenter)
        self.bB5.clicked.connect(lambda: self.calc(self.bB5.text()))

        self.bB6 = QPushButton("6")
        self.bB6.setFont(QFont('Arial', 14))
        self.bB6.setFixedSize(100, 100)
        self.mainlayout2.addWidget(self.bB6, 2, 2, QtCore.Qt.AlignCenter)
        self.bB6.clicked.connect(lambda: self.calc(self.bB6.text()))

        self.bBm = QPushButton("-")
        self.bBm.setFont(QFont('Arial', 14))
        self.bBm.setFixedSize(100, 100)
        self.mainlayout2.addWidget(self.bBm, 2, 3, QtCore.Qt.AlignCenter)
        self.bBm.clicked.connect(lambda: self.calc(self.bBm.text()))

        self.bB7 = QPushButton("7")
        self.bB7.setFont(QFont('Arial', 14))
        self.bB7.setFixedSize(100, 100)
        self.mainlayout2.addWidget(self.bB7, 3, 0, QtCore.Qt.AlignCenter)
        self.bB7.clicked.connect(lambda: self.calc(self.bB7.text()))

        self.bB8 = QPushButton("8")
        self.bB8.setFont(QFont('Arial', 14))
        self.bB8.setFixedSize(100, 100)
        self.mainlayout2.addWidget(self.bB8, 3, 1, QtCore.Qt.AlignCenter)
        self.bB8.clicked.connect(lambda: self.calc(self.bB8.text()))

        self.bB9 = QPushButton("9")
        self.bB9.setFont(QFont('Arial', 14))
        self.bB9.setFixedSize(100, 100)
        self.mainlayout2.addWidget(self.bB9, 3, 2, QtCore.Qt.AlignCenter)
        self.bB9.clicked.connect(lambda: self.calc(self.bB9.text()))

        self.bBx = QPushButton("×")
        self.bBx.setFont(QFont('Arial', 14))
        self.bBx.setFixedSize(100, 100)
        self.mainlayout2.addWidget(self.bBx, 3, 3, QtCore.Qt.AlignCenter)
        self.bBx.clicked.connect(lambda: self.calc(self.bBx.text()))

        self.bB0 = QPushButton("0")
        self.bB0.setFont(QFont('Arial', 14))
        self.bB0.setFixedSize(100, 100)
        self.mainlayout2.addWidget(self.bB0, 4, 0, QtCore.Qt.AlignCenter)
        self.bB0.clicked.connect(lambda: self.calc(self.bB0.text()))

        self.bBd = QPushButton(".")
        self.bBd.setFont(QFont('Arial', 14))
        self.bBd.setFixedSize(100, 100)
        self.mainlayout2.addWidget(self.bBd, 4, 1, QtCore.Qt.AlignCenter)
        self.bBd.clicked.connect(lambda: self.calc(self.bBd.text()))

        self.bBDelete = QPushButton('Del')
        self.bBDelete.setFont(QFont('Arial', 14))
        self.bBDelete.setFixedSize(100, 100)
        self.mainlayout2.addWidget(self.bBDelete, 4, 2, QtCore.Qt.AlignCenter)
        self.bBDelete.clicked.connect(lambda: self.calc(self.bBDelete.text()))

        self.bBD = QPushButton("÷")
        self.bBD.setFont(QFont('Arial', 14))
        self.bBD.setFixedSize(100, 100)
        self.mainlayout2.addWidget(self.bBD, 4, 3, QtCore.Qt.AlignCenter)
        self.bBD.clicked.connect(lambda: self.calc(self.bBD.text()))

        self.bBE = QPushButton('=')
        self.bBE.setFont(QFont('Arial', 14))
        self.bBE.setFixedSize(430, 100)
        self.bBE.clicked.connect(lambda: self.calc(self.bBE.text()))

        self.mainlayout.addLayout(self.mainlayout1)
        self.mainlayout.addLayout(self.mainlayout2)
        self.mainlayout.addWidget(self.bBE)

        self.setLayout(self.mainlayout)
        self.texteq = ""
        self.flag=False

    def calc(self, text):
        if self.flag:
            self.screen.setText("")
            self.texteq = ""
            self.flag = False
        if text in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '×', '÷', '.', '(', ')', '%'):
            if text in ('-', '+', '÷', '×','%'):
                textS = self.screen.text()
                self.screen.setText(textS + " " + text + " ")
                if text == '×':
                    self.texteq += '*'
                elif text == '÷':
                    self.texteq += '/'
                elif text == '%':
                    self.texteq += '*(1/100)'
                else:
                    self.texteq += text
            else:
                textS = self.screen.text()
                self.screen.setText(textS + text)
                self.texteq += text
        elif text == "C":
            self.screen.setText("")
            self.texteq = ""
        elif text == "Del":
            textS = self.screen.text()
            if textS != "":
                if textS[-1] != '%':
                    x = list(textS)
                    while x[-1] == " ":
                        x.pop()
                    x.pop()
                    if len(x) != 0:
                        if x[-1] == " ":
                            x.pop()
                    textS = "".join(x)
                    self.screen.setText(textS)

                    z = list(self.texteq)
                    z.pop()
                    self.texteq = "".join(z)
                else:
                    x = list(textS)
                    while x[-1] == " ":
                        x.pop()
                    x.pop()
                    if len(x) != 0:
                        if x[-1] == " ":
                            x.pop()
                    textS = "".join(x)
                    self.screen.setText(textS)

                    z = list(self.texteq)
                    for i in range(8):
                        z.pop()
                    self.texteq = "".join(z)
        elif text == "=":
            self.flag=True
            print(self.texteq)
            try:
                sol = eval(self.texteq)
                self.screen.setText(str(sol))
                self.texteq=""
            except:
                self.screen.setText("Equation Error")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(1, 32, 48))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(19, 103, 138))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.black)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.black)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, QColor(35, 35, 35))
    dark_palette.setColor(QPalette.Active, QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.darkGray)
    dark_palette.setColor(QPalette.Disabled, QPalette.WindowText, Qt.darkGray)
    dark_palette.setColor(QPalette.Disabled, QPalette.Text, Qt.darkGray)
    dark_palette.setColor(QPalette.Disabled, QPalette.Light, QColor(53, 53, 53))

    app.setStyle('Breeze')
    app.setPalette(dark_palette)
    w = Main_window()
    w.show()
    sys.exit(app.exec_())
