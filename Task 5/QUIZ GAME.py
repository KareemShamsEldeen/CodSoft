import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QGroupBox, QRadioButton, QMessageBox
from PyQt5.QtGui import QPalette, QColor, QIcon
from PyQt5.QtCore import Qt


class QuizGame(QMainWindow):
    def __init__(self, questions):
        super().__init__()
        self.questions = questions
        self.score = 0
        self.current_question = 0

        self.setWindowTitle("Quiz Game")
        self.icon=QIcon('images/pngwing.com(4).png')
        self.setWindowIcon(QIcon('images/pngwing.com(4).png'))
        self.setGeometry(100, 100, 400, 300)

        # Set the dark palette
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
        self.setPalette(dark_palette)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.question_label = QLabel()
        self.question_label.setAlignment(Qt.AlignHCenter)
        # -font-
        main_label_font = self.question_label.font()
        main_label_font.setPointSize(18)
        main_label_font.bold()
        main_label_font.italic()
        self.question_label.setFont(main_label_font)
        self.layout.addWidget(self.question_label)

        self.choices_group = QGroupBox()
        self.choices_layout = QVBoxLayout()
        self.choices_group.setLayout(self.choices_layout)
        self.layout.addWidget(self.choices_group)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.check_answer)
        self.layout.addWidget(self.submit_button)

        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.next_question)
        self.next_button.setEnabled(False)
        self.layout.addWidget(self.next_button)

        self.play_again_button = QPushButton("Play Again")
        self.play_again_button.clicked.connect(self.play_again)
        self.play_again_button.setEnabled(False)
        self.layout.addWidget(self.play_again_button)

        self.show_question()

    def show_question(self):
        self.next_button.setEnabled(False)
        self.submit_button.setEnabled(True)

        question = self.questions[self.current_question]
        self.question_label.setText(question["question"])

        for radio_button in self.findChildren(QRadioButton):
            radio_button.setChecked(False)
            self.choices_group.layout().removeWidget(radio_button)
            radio_button.deleteLater()

        for i, choice in enumerate(question["choices"]):
            radio_button = QRadioButton(choice)
            self.choices_group.layout().addWidget(radio_button)

    def check_answer(self):
        self.submit_button.setEnabled(False)
        self.next_button.setEnabled(True)

        question = self.questions[self.current_question]
        user_answer = ""
        for radio_button in self.choices_group.findChildren(QRadioButton):
            if radio_button.isChecked():
                user_answer = radio_button.text()
                break

        if user_answer.lower() == question["answer"].lower():
            self.score += 1
            QMessageBox.information(self, "Correct", "Your answer is correct!", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Incorrect", f"Your answer is incorrect. The correct answer is: {question['answer']}", QMessageBox.Ok)

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        QMessageBox.information(self, "Quiz Finished", f"Quiz finished!\nFinal Score: {self.score}/{len(self.questions)}", QMessageBox.Ok)
        self.submit_button.setEnabled(False)
        self.next_button.setEnabled(False)
        self.play_again_button.setEnabled(True)

    def play_again(self):
        self.score = 0
        self.current_question = 0
        self.show_question()
        self.play_again_button.setEnabled(False)


if __name__ == "__main__":
    # Quiz questions
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["London", "Paris", "Berlin", "Rome"],
            "answer": "Paris"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "choices": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
            "answer": "Leonardo da Vinci"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "choices": ["Mars", "Jupiter", "Earth", "Saturn"],
            "answer": "Jupiter"
        },
        {
            "question": "Which country won the 2018 FIFA World Cup?",
            "choices": ["Germany", "Brazil", "France", "Argentina"],
            "answer": "France"
        }
    ]

    app = QApplication(sys.argv)
    game = QuizGame(questions)
    game.show()
    sys.exit(app.exec_())