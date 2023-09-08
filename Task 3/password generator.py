import qrcode
from PyQt5 import *
import sys
import random

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, \
    QTextEdit, QLineEdit, QListWidget, QSlider, QCheckBox
from PyQt5 import QtGui
import zxcvbn
import collections


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

small_letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

Cap_letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

class Main_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ZEUS PG")
        self.icon=QIcon('images/pngwing.com(3).png')
        self.setWindowIcon(QIcon('images/pngwing.com(3).png'))
        self.setMinimumSize(650,600)
        self.setMaximumSize(650,600)
        #layouts
        self.mainlayout = QVBoxLayout()
        self.mainlayout1 = QVBoxLayout()
        self.slidelayout = QHBoxLayout()
        self.Hlayout1 = QHBoxLayout()#checkbox1
        self.Hlayout2 = QHBoxLayout()#checkbox2
        self.Hlayout4 = QHBoxLayout()#Ex
        self.Hlayout5 = QHBoxLayout()#User
        self.Hlayout6 = QHBoxLayout()#link
        self.Hlayout7 = QHBoxLayout()#pass strength
        self.Hlayout8 = QHBoxLayout()#strength
        self.Hlayout3 = QHBoxLayout()#buttons
        self.Hlayout9 = QHBoxLayout()#qr

        self.password = ""

        #labels
        self.Headlabel = QLabel("Password Generator")
        self.Headlabel.setAlignment(Qt.AlignHCenter)
        # -font-
        main_label_font = self.Headlabel.font()
        main_label_font.setPointSize(20)
        main_label_font.bold()
        main_label_font.italic()
        self.Headlabel.setFont(main_label_font)
        #--
        self.Headlabel.setStyleSheet("QLabel"
                                  "{"
                                  "padding-bottom : 15px ; "
                                  "}")
        self.mainlayout1.addWidget(self.Headlabel)
        # ----
        self.label1 = QLabel("Password Length:8")
        self.label1.setAlignment(Qt.AlignLeft)
        # -font-
        label1_font = self.Headlabel.font()
        label1_font.setPointSize(10)
        label1_font.bold()
        label1_font.italic()
        self.label1.setFont(label1_font)
        #----
        self.index5 = QLabel("8")
        self.index5.setAlignment(Qt.AlignLeft)
        # -font-
        index5_font = self.index5.font()
        index5_font.setPointSize(10)
        index5_font.italic()
        self.index5.setFont(index5_font)
        self.index5.setStyleSheet("QLabel"
                                  "{"
                                  "padding-left : -1px ; "
                                  "}")
        #----
        self.slidelayout.addWidget(self.index5)
        # ----

        self.index80 = QLabel("80")
        self.index80.setAlignment(Qt.AlignRight)
        # -font-
        index80_font = self.index80.font()
        index80_font.setPointSize(10)
        index80_font.italic()
        self.index80.setFont(index80_font)
        self.index80.setStyleSheet("QLabel"
                                  "{"
                                  "padding-right : 1px ; "
                                  "}")
        self.slidelayout.addWidget(self.index80)
        #----
        self.label2 = QLabel("Enter the characters to exclude it :")
        self.label2.setAlignment(Qt.AlignLeft)
        # -font-
        label2_font = self.label2.font()
        label2_font.setPointSize(10)
        label2_font.bold()
        label2_font.italic()
        self.label2.setFont(label2_font)
        self.label2.setStyleSheet("QLabel"
                                  "{"
                                  "padding-top : 10px ; "
                                  "}")
        self.Hlayout4.addWidget(self.label2)
        #----
        self.label3 = QLabel("Username :")
        self.label3.setAlignment(Qt.AlignLeft)
        # -font-
        label3_font = self.label3.font()
        label3_font.setPointSize(10)
        label3_font.bold()
        label3_font.italic()
        self.label3.setFont(label3_font)
        self.label3.setStyleSheet("QLabel"
                                  "{"
                                  "padding-top : 10px ; "
                                  "}")
        self.Hlayout5.addWidget(self.label3)
        #----
        self.label4 = QLabel("URL :")
        self.label4.setAlignment(Qt.AlignLeft)
        # -font-
        label4_font = self.label4.font()
        label4_font.setPointSize(10)
        label4_font.bold()
        label4_font.italic()
        self.label4.setFont(label4_font)
        self.label4.setStyleSheet("QLabel"
                                  "{"
                                  "padding-top : 10px ; "
                                  "}")
        self.Hlayout6.addWidget(self.label4)
        #----
        self.label5 = QLabel("Password :")
        self.label5.setAlignment(Qt.AlignLeft)
        self.label5.wordWrap()
        # -font-
        label5_font = self.label5.font()
        label5_font.setPointSize(10)
        label5_font.bold()
        label5_font.italic()
        self.label5.setFont(label5_font)
        self.label5.setStyleSheet("QLabel"
                                  "{"
                                  "padding-top : 10px ; "
                                  "}")
        self.Hlayout7.addWidget(self.label5)
        #----
        self.label6 = QLabel("Strength :")
        self.label6.setAlignment(Qt.AlignLeft)
        self.label6.wordWrap()
        # -font-
        label6_font = self.label6.font()
        label6_font.setPointSize(10)
        label6_font.bold()
        label6_font.italic()
        self.label6.setFont(label6_font)
        self.label6.setStyleSheet("QLabel"
                                  "{"
                                  "padding-top : 10px ; "
                                  "}")
        self.Hlayout8.addWidget(self.label6)
        #----
        #----
        self.label7 = QLabel()
        self.label7.setAlignment(Qt.AlignCenter)
        self.label7.setStyleSheet("QLabel"
                                  "{"
                                  "padding-top : 10px ; "
                                  "}")
        self.Hlayout9.addWidget(self.label7)
        #----

        #Widgets
        self.slider=QSlider(Qt.Horizontal)
        self.slider.setMinimum(8)
        self.slider.setValue(8)
        self.slider.setMaximum(80)
        self.slider.setSingleStep(3)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.mainlayout1.addWidget(self.slider)
        self.mainlayout1.addLayout(self.slidelayout)
        self.mainlayout1.setAlignment(Qt.AlignTop)
        self.slider.valueChanged.connect(self.SlidevalueChanged)
        self.mainlayout1.addWidget(self.label1)

        #----
        self.CboxAs = QCheckBox()
        self.CboxAs.setText("Alphabet Small")
        # -font-
        CboxAs_font = self.CboxAs.font()
        CboxAs_font.setPointSize(10)
        CboxAs_font.italic()
        self.CboxAs.setFont(CboxAs_font)
        self.CboxAs.setStyleSheet("QCheckBox"
                                  "{"
                                  "padding-left : 10px ; "
                                  "padding-top : 10px ; "
                                  "}")
        self.Hlayout1.addWidget(self.CboxAs)
        #----
        self.CboxAc = QCheckBox()
        self.CboxAc.setText("Alphabet Capital")
        # -font-
        CboxAc_font = self.CboxAc.font()
        CboxAc_font.setPointSize(10)
        CboxAc_font.italic()
        self.CboxAc.setFont(CboxAc_font)
        self.CboxAc.setStyleSheet("QCheckBox"
                                  "{"
                                  "padding-left : 10px ; "
                                  "padding-top : 10px ; "
                                  "}")
        self.Hlayout1.addWidget(self.CboxAc)
        #----
        self.Cboxn = QCheckBox()
        self.Cboxn.setText("Numbers")
        # -font-
        Cboxn_font = self.Cboxn.font()
        Cboxn_font.setPointSize(10)
        Cboxn_font.italic()
        self.Cboxn.setFont(Cboxn_font)
        self.Cboxn.setStyleSheet("QCheckBox"
                                  "{"
                                  "padding-left : 10px ; "
                                  "padding-top : 10px ; "
                                  "}")
        self.Hlayout2.addWidget(self.Cboxn)
        #----
        self.CboxSC = QCheckBox()
        self.CboxSC.setText("Special Characters")
        # -font-
        CboxSC_font = self.CboxSC.font()
        CboxSC_font.setPointSize(10)
        CboxSC_font.italic()
        self.CboxSC.setFont(CboxSC_font)
        self.CboxSC.setStyleSheet("QCheckBox"
                                  "{"
                                  "padding-left : 10px ; "
                                  "padding-top : 10px ; "
                                  "}")
        self.Hlayout2.addWidget(self.CboxSC)
        #----
        self.ExCh = QLineEdit()
        self.ExCh.setStyleSheet("QLineEdit"
                                  "{"
                                  "margin-top : 10px ; "
                                  "}")
        self.Hlayout4.addWidget(self.ExCh)
        #----
        self.user = QLineEdit()
        self.user.setStyleSheet("QLineEdit"
                                  "{"
                                  "margin-top : 10px ; "
                                  "}")
        self.Hlayout5.addWidget(self.user)
        #----
        self.url = QLineEdit()
        self.url.setStyleSheet("QLineEdit"
                                  "{"
                                  "margin-top : 10px ; "
                                  "}")
        self.Hlayout6.addWidget(self.url)
        #----
        self.btn1 = QPushButton()
        self.btn1.setText('Generate')
        # -font-
        btn1_font = self.btn1.font()
        btn1_font.setPointSize(10)
        btn1_font.setBold(True)
        btn1_font.italic()
        self.btn1.setFont(Cboxn_font)
        self.btn1.setFixedSize(80,45)
        self.btn1.setStyleSheet("QPushButton"
                       "{"
                       "margin-top : 10px ; "
                       "}")
        self.btn1.clicked.connect(lambda: self.gen())
        self.Hlayout3.addWidget(self.btn1)
        #----
        self.btn2 = QPushButton()
        self.btn2.setText('Make Qr')
        # -font-
        btn2_font = self.btn2.font()
        btn2_font.setPointSize(10)
        btn2_font.setBold(True)
        btn2_font.italic()
        self.btn2.setFont(Cboxn_font)
        self.btn2.setFixedSize(80,45)
        self.btn2.setStyleSheet("QPushButton"
                       "{"
                       "margin-top : 10px ; "
                       "}")
        self.btn2.clicked.connect(lambda: self.makeQR())
        self.Hlayout3.addWidget(self.btn2)



        self.mainlayout1.addLayout(self.Hlayout1)
        self.mainlayout1.addLayout(self.Hlayout2)
        self.mainlayout1.addLayout(self.Hlayout4)
        self.mainlayout1.addLayout(self.Hlayout5)
        self.mainlayout1.addLayout(self.Hlayout6)
        self.mainlayout1.addLayout(self.Hlayout7)
        self.mainlayout1.addLayout(self.Hlayout8)
        self.mainlayout1.addLayout(self.Hlayout3)
        self.mainlayout1.addLayout(self.Hlayout9)
        self.mainlayout.addLayout(self.mainlayout1)
        self.setLayout(self.mainlayout)


        self.txts="Password Length:"
        self.cur_index=8
    def SlidevalueChanged(self,i):
        self.label1.setText(self.txts + str(i))
        self.cur_index=i

    def gen(self):
        self.password = ""
        self.ExcludeChars = list(self.ExCh.text().strip(" "))

        if collections.Counter(self.ExcludeChars) == collections.Counter(small_letters) and self.CboxAs.isChecked():
            error = QMessageBox()
            error.setWindowTitle("Error!!")
            error.setIcon(QMessageBox.Critical)
            error.setStyleSheet("color:white;background: rgb(1, 32, 48)")
            error.addButton(QMessageBox.Ok)
            button = error.button(QMessageBox.Ok)
            button.setStyleSheet("background-color: rgb(19, 103, 138);")
            error.setWindowIcon(QIcon('images/error.png'))
            error.setText("You exclude every characters in Alphabet Small,So unchecked it")
            error.exec()
        elif collections.Counter(self.ExcludeChars) == collections.Counter(Cap_letters) and self.CboxAc.isChecked():
            error = QMessageBox()
            error.setWindowTitle("Error!!")
            error.setIcon(QMessageBox.Critical)
            error.setStyleSheet("color:white;background: rgb(1, 32, 48)")
            error.addButton(QMessageBox.Ok)
            button = error.button(QMessageBox.Ok)
            button.setStyleSheet("background-color: rgb(19, 103, 138);")
            error.setWindowIcon(QIcon('images/error.png'))
            error.setText("You exclude every characters in Alphabet Capital,So unchecked it")
            error.exec()
        elif collections.Counter(self.ExcludeChars) == collections.Counter(numbers) and self.Cboxn.isChecked():
            error = QMessageBox()
            error.setWindowTitle("Error!!")
            error.setIcon(QMessageBox.Critical)
            error.setStyleSheet("color:white;background: rgb(1, 32, 48)")
            error.addButton(QMessageBox.Ok)
            button = error.button(QMessageBox.Ok)
            button.setStyleSheet("background-color: rgb(19, 103, 138);")
            error.setWindowIcon(QIcon('images/error.png'))
            error.setText("You exclude all the numbers,So unchecked it")
            error.exec()
        elif collections.Counter(self.ExcludeChars) == collections.Counter(symbols) and self.CboxSC.isChecked():
            error = QMessageBox()
            error.setWindowTitle("Error!!")
            error.setIcon(QMessageBox.Critical)
            error.setStyleSheet("color:white;background: rgb(1, 32, 48)")
            error.addButton(QMessageBox.Ok)
            button = error.button(QMessageBox.Ok)
            button.setStyleSheet("background-color: rgb(19, 103, 138);")
            error.setWindowIcon(QIcon('images/error.png'))
            error.setText("You exclude all the Special Characters,So unchecked it")
            error.exec()
        elif self.CboxAs.isChecked() or self.CboxAc.isChecked() or self.Cboxn.isChecked() or self.CboxSC.isChecked():
            password_list = []
            i=1
            while i < self.cur_index + 1:
                if self.CboxAs.isChecked():
                    char = random.choice(small_letters)
                    if char not in self.ExcludeChars:
                        password_list.append(char)
                        i += 1
                if self.CboxAc.isChecked():
                    char = random.choice(Cap_letters)
                    if char not in self.ExcludeChars:
                        password_list.append(char)
                        i += 1
                if self.Cboxn.isChecked():
                    char = random.choice(numbers)
                    if char not in self.ExcludeChars:
                        password_list.append(char)
                        i += 1
                if self.CboxSC.isChecked():
                    char = random.choice(symbols)
                    if char not in self.ExcludeChars:
                        password_list.append(char)
                        i += 1
            random.shuffle(password_list)

            for i in range(self.cur_index):
                self.password += password_list[i]

            self.label5.setText(f"Password : {self.password}")
            self.label5.adjustSize()
            print(f"Your random password to use is: {self.password}")
            # Strength of Password
            self.strength = zxcvbn.zxcvbn(self.password)
            self.score = self.strength["score"]
            if self.score == 4:
                self.label6.setText("Strength : Very Strong")
            elif self.score == 3:
                self.label6.setText("Strength : Strong")
            elif self.score == 2:
                self.label6.setText("Strength : Moderate")
            elif self.score == 1:
                self.label6.setText("Strength : Weak")
            elif self.score == 0:
                self.label6.setText("Strength : Very Weak")
        else :
            error = QMessageBox()
            error.setWindowTitle("Error!!")
            error.setIcon(QMessageBox.Critical)
            error.setStyleSheet("color:white;background: rgb(1, 32, 48)")
            error.addButton(QMessageBox.Ok)
            button = error.button(QMessageBox.Ok)
            button.setStyleSheet("background-color: rgb(19, 103, 138);")
            error.setWindowIcon(QIcon('images/error.png'))
            error.setText("Choose how you need to customize ur pass")
            error.exec()

    def makeQR(self):
        if self.password == "":
            error = QMessageBox()
            error.setWindowTitle("Error!!")
            error.setIcon(QMessageBox.Critical)
            error.setStyleSheet("color:white;background: rgb(1, 32, 48)")
            error.addButton(QMessageBox.Ok)
            button = error.button(QMessageBox.Ok)
            button.setStyleSheet("background-color: rgb(19, 103, 138);")
            error.setWindowIcon(QIcon('images/error.png'))
            error.setText("Generate Password")
            error.exec()
        else:
            # make QR
            self.textqe="Password :"+self.password + "\n" +"Username :"+self.user.text()+ "\n" +"URL :"+self.url.text()+ "\n"
            QR = qrcode.QRCode(version=1, box_size=4, border=1)
            QR.add_data(self.textqe)
            QR.make()
            img = QR.make_image(fill_color='black', back_color='white')
            img.save('images/QR.png')
            # Display QR
            self.im = QPixmap("images/QR.png")
            self.label7.setPixmap(self.im)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyle('Breeze')
    app.setPalette(dark_palette)
    w = Main_window()
    w.show()
    sys.exit(app.exec_())
