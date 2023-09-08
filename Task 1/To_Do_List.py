from PyQt5 import *
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, \
    QTextEdit, QLineEdit, QListWidget
from PyQt5 import QtGui

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
class options_window(QWidget):
    def __init__(self,Tasks,task,w):
        super().__init__()
        self.Ctasks = Tasks
        self.Ctask = task
        self.win = Main_window()
        self.win = w

        self.setWindowTitle("Options")
        self.setFixedWidth(400)
        self.setFixedHeight(100)
        self.setWindowIcon(QtGui.QIcon('images/logo22.png'))
        self.mainlayout = QVBoxLayout()
        self.mainlayout1 = QHBoxLayout()


        self.label = QLabel()
        self.label.setText(f'Task : {task}')
        self.label.setAlignment(Qt.AlignHCenter)

        main_label_font = self.label.font()
        main_label_font.setPointSize(15)
        main_label_font.bold()
        main_label_font.italic()

        self.label.setFont(main_label_font)
        self.mainlayout.addWidget(self.label)

        self.btn1 = QPushButton()
        self.btn1.setText('Edit')
        self.btn1.clicked.connect(lambda: self.Edit_task())

        self.btn2 = QPushButton()
        self.btn2.setText('Delete')
        self.btn2.clicked.connect(lambda: self.Delete_task())


        self.mainlayout1.addWidget(self.btn1)
        self.mainlayout1.addWidget(self.btn2)

        self.mainlayout.addLayout(self.mainlayout1)
        self.setLayout(self.mainlayout)

        self.EW = QWidget()
        self.EW.setWindowIcon(QtGui.QIcon('images/logo22.png'))
        self.EW.setWindowTitle("Edit Task")
        self.mainlayout3 = QHBoxLayout()

        self.label3 = QLabel()
        self.label3.setText("Add New Task Name")

        sec_label_font = self.label3.font()
        sec_label_font.setPointSize(10)
        sec_label_font.bold()
        sec_label_font.italic()

        self.label3.setFont(sec_label_font)

        self.task_nname = QLineEdit()


        self.btn3 = QPushButton()
        self.btn3.setText('Edit')
        self.btn3.clicked.connect(lambda: self.Edit_BtnF())

        self.mainlayout3.addWidget(self.label3)
        self.mainlayout3.addWidget(self.task_nname)
        self.mainlayout3.addWidget(self.btn3)
        self.EW.setLayout(self.mainlayout3)


    def Delete_task(self):
        self.Ctasks.remove(self.Ctask)
        self.close()
        self.win.update()

    def Edit_task(self):
        self.EW.show()


    def Edit_BtnF(self):
        if self.task_nname.text() != "":
            self.i=self.Ctasks.index(self.Ctask)
            self.Ctasks[int(self.i)]=self.task_nname.text()
            self.Ctask=self.task_nname.text()
            Information = QMessageBox()
            Information.setWindowTitle("Edited")
            Information.setIcon(QMessageBox.Information)
            Information.setStyleSheet("color:white;background: rgb(1, 32, 48)")
            Information.setWindowIcon(QIcon('images/logo22.png'))
            Information.addButton(QMessageBox.Ok)
            button = Information.button(QMessageBox.Ok)
            button.setStyleSheet("background-color: rgb(19, 103, 138);")
            Information.setText("Edited successfully")
            Information.exec()
            self.label.setText(f'Task : {self.Ctasks[int(self.i)]}')
            self.EW.close()
            self.win.update()
        else:
            error = QMessageBox()
            error.setWindowTitle("Error!!")
            error.setIcon(QMessageBox.Critical)
            error.setStyleSheet("color:white;background: rgb(1, 32, 48)")
            error.addButton(QMessageBox.Ok)
            button = error.button(QMessageBox.Ok)
            button.setStyleSheet("background-color: rgb(19, 103, 138);")
            error.setWindowIcon(QIcon('images/error.png'))
            error.setText("ُEnter Valid Name")
            error.exec()


class Main_window(QWidget):
    def __init__(self):
        super().__init__()
        self.Tasks = ['t1','t2']
        self.setWindowTitle("ZEUS")
        self.setWindowIcon(QtGui.QIcon('images/logo22.png'))

        self.labelpic = QLabel()
        self.pixmap = QPixmap('images/logo2.png')
        self.smaller_pixmap = self.pixmap.scaled(320, 320, Qt.KeepAspectRatio)
        self.labelpic.setPixmap(self.smaller_pixmap)
        self.labelpic.setAlignment(Qt.AlignHCenter)

        self.label = QLabel()
        self.label.setText("To Do List")
        self.label.setAlignment(Qt.AlignHCenter)

        main_label_font = self.label.font()
        main_label_font.setPointSize(20)
        main_label_font.bold()
        main_label_font.italic()

        self.label.setFont(main_label_font)

        self.label1 = QLabel()
        sec_label_font = self.label1.font()
        sec_label_font.setPointSize(10)
        sec_label_font.bold()
        sec_label_font.italic()

        list_label_font = self.label1.font()
        list_label_font.setPointSize(15)
        list_label_font.bold()

        self.listwidget = QListWidget()
        self.listwidget.setFont(list_label_font)


        self.mainlayout = QVBoxLayout()
        self.mainlayout1 = QHBoxLayout()
        self.mainlayout2 = QHBoxLayout()




        self.label1.setText("Add Task")
        self.label1.setFont(sec_label_font)

        self.task_name=QLineEdit()


        self.btn1 = QPushButton()
        self.btn1.setText('ADD')
        self.btn1.clicked.connect(lambda: self.Add_task())


        self.label2 = QLabel()
        self.label2.setText("label2")


        self.mainlayout1.addWidget(self.label1)
        self.mainlayout1.addWidget(self.task_name)
        self.mainlayout1.addWidget(self.btn1)

        self.mainlayout2.addWidget(self.listwidget)
        self.listwidget.clicked.connect(self.clicked)

        self.mainlayout.addWidget(self.labelpic)
        self.mainlayout.addWidget(self.label)
        self.mainlayout.addLayout(self.mainlayout1)
        self.mainlayout.addLayout(self.mainlayout2)
        self.setLayout(self.mainlayout)

    def Add_task(self):
        if  self.task_name.text() != "":
            task_name = self.task_name.text()
            self.Tasks.append(task_name)
            self.listwidget.clear()
            count = 1
            for task in self.Tasks:
                self.listwidget.insertItem(count - 1, f'{task}')
                count += 1
            Information = QMessageBox()
            Information.setWindowTitle("Added")
            Information.setIcon(QMessageBox.Information)
            Information.setStyleSheet("color:white;background: rgb(1, 32, 48)")
            Information.setWindowIcon(QIcon('images/logo22.png'))

            Information.addButton(QMessageBox.Ok)
            button = Information.button(QMessageBox.Ok)
            button.setStyleSheet("background-color: rgb(19, 103, 138);")

            Information.setText("Added successfully")
            Information.exec()
        else:
            error = QMessageBox()
            error.setWindowTitle("Error!!")
            error.setIcon(QMessageBox.Critical)
            error.addButton(QMessageBox.Ok)
            button = error.button(QMessageBox.Ok)
            button.setStyleSheet("background-color: rgb(19, 103, 138);")
            error.setStyleSheet("color:white;background: rgb(1, 32, 48)")
            error.setWindowIcon(QIcon('images/error.png'))
            error.setText("Enter Valid Name")
            error.exec()


    def update(self):
        self.listwidget.clear()
        count = 1
        for task in self.Tasks:
            self.listwidget.insertItem(count - 1, f'{task}')
            count += 1


    def clicked(self, qmodelindex):
        item = self.listwidget.currentItem()
        print(item.text())

        self.options = options_window(self.Tasks,item.text(),self)
        self.options.show()

        self.Tasks = self.options.Ctasks

        self.listwidget.clear()
        count = 1
        for task in self.Tasks:
            self.listwidget.insertItem(count - 1, f'{task}')
            count += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)


    app.setStyle('Breeze')
    app.setPalette(dark_palette)
    w = Main_window()
    w.show()
    sys.exit(app.exec_())
