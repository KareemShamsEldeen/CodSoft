from PyQt5 import *
import sys
import random

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, \
    QTextEdit, QLineEdit, QListWidget, QSlider, QCheckBox
from PyQt5 import QtGui
import requests

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

class Main_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ZEUS WF")
        self.icon=QIcon('images/pngwing.com(2).png')
        self.setWindowIcon(QIcon('images/pngwing.com(2).png'))
        #self.setMinimumSize(650,600)
        #self.setMaximumSize(650,600)
        #layouts
        self.mainlayout = QVBoxLayout()
        self.mainlayout1 = QVBoxLayout()
        self.Hlayout = QHBoxLayout()

        #labels
        self.Headlabel = QLabel("WEATHER FORECAST")
        self.Headlabel.setAlignment(Qt.AlignHCenter)
        # -font-
        main_label_font = self.Headlabel.font()
        main_label_font.setPointSize(20)
        main_label_font.bold()
        main_label_font.italic()
        self.Headlabel.setFont(main_label_font)
        self.mainlayout.addWidget(self.Headlabel)
        #--
        self.label1 = QLabel("Country name:")
        self.label1.setAlignment(Qt.AlignLeft)
        # -font-
        label1_font = self.label1.font()
        label1_font.setPointSize(10)
        label1_font.italic()
        self.label1.setFont(label1_font)
        self.Hlayout.addWidget(self.label1)
        #--
        self.label2 = QLabel("Description:")
        self.label2.setAlignment(Qt.AlignLeft)
        # -font-
        label1_font = self.label2.font()
        label1_font.setPointSize(10)
        label1_font.italic()
        self.label2.setFont(label1_font)
        self.mainlayout1.addWidget(self.label2)
        #--
        self.label3 = QLabel("Temperature:")
        self.label3.setAlignment(Qt.AlignLeft)
        # -font-
        label1_font = self.label3.font()
        label1_font.setPointSize(10)
        label1_font.italic()
        self.label3.setFont(label1_font)
        self.mainlayout1.addWidget(self.label3)
        #--
        self.label4 = QLabel("Feels Like:")
        self.label4.setAlignment(Qt.AlignLeft)
        # -font-
        label1_font = self.label4.font()
        label1_font.setPointSize(10)
        label1_font.italic()
        self.label4.setFont(label1_font)
        self.mainlayout1.addWidget(self.label4)
        #--
        self.label5 = QLabel("Pressure:")
        self.label5.setAlignment(Qt.AlignLeft)
        # -font-
        label1_font = self.label5.font()
        label1_font.setPointSize(10)
        label1_font.italic()
        self.label5.setFont(label1_font)
        self.mainlayout1.addWidget(self.label5)
        #--
        self.label6 = QLabel("Humidity:")
        self.label6.setAlignment(Qt.AlignLeft)
        # -font-
        label1_font = self.label6.font()
        label1_font.setPointSize(10)
        label1_font.italic()
        self.label6.setFont(label1_font)
        self.mainlayout1.addWidget(self.label6)
        #----

        # Widgets
        self.country = QLineEdit()
        self.country.setText("Cairo, EG")
        self.Hlayout.addWidget(self.country)
        self.mainlayout.addLayout(self.Hlayout)
        #--
        self.btn1 = QPushButton()
        self.btn1.setText('Get Weather')
        # -font-
        btn1_font = self.btn1.font()
        btn1_font.setPointSize(10)
        btn1_font.setBold(True)
        btn1_font.italic()
        self.btn1.setFont(btn1_font)
       # self.btn1.setFixedSize(80,45)
        self.btn1.clicked.connect(lambda: self.get())
        self.mainlayout.addWidget(self.btn1)
        self.mainlayout.addLayout(self.mainlayout1)


        self.setLayout(self.mainlayout)


    def get(self):
        if self.country.text()=="":
            error = QMessageBox()
            error.setWindowTitle("Error!!")
            error.setIcon(QMessageBox.Critical)
            error.setStyleSheet("color:white;background: rgb(1, 32, 48)")
            error.addButton(QMessageBox.Ok)
            button = error.button(QMessageBox.Ok)
            button.setStyleSheet("background-color: rgb(19, 103, 138);")
            error.setWindowIcon(QIcon('images/error.png'))
            error.setText("You need to enter a country's name")
            error.exec()
        else:
            api_key = '0a27ab9ef19f644b4e0a01bb78884573'
            city_name = self.country.text()

            api_endpoint = f' https://api.openweathermap.org/data/2.5/weather?q={city_name},uk&APPID=0a27ab9ef19f644b4e0a01bb78884573'
            # query_params = {'q': city_name, 'appid': api_key, 'units': 'metric'}

            response = requests.get(api_endpoint)

            if response.status_code == 200:
                data = response.json()
                print(data)
                # Handle response data
                temperaturef = data['main']['temp']
                self.label3.setText("Temperature: " + str(temperaturef)+"°F")

                feels_likef = data['main']['feels_like']
                self.label4.setText("Feels Like: " + str(feels_likef)+"°F")

                des = data['weather'][0]['description']
                self.label2.setText("Description: " + des)

                pressure = data['main']['pressure']
                self.label5.setText("Pressure: " + str(pressure))

                Humidity = data['main']['humidity']
                self.label6.setText("Humidity: " + str(Humidity))


            else:
                self.label3.setText("Temperature: ")

                self.label4.setText("Feels Like: ")

                self.label2.setText("Description: Error,try again")

                self.label5.setText("Pressure: ")

                self.label6.setText("Humidity: ")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyle('Breeze')
    app.setPalette(dark_palette)
    w = Main_window()
    w.show()
    sys.exit(app.exec_())
