from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint
app = QApplication([])
main_win = QWidget()


#создание элементов интерфейса
text = QLabel("Нажми чтоб узнать победителя")
button = QPushButton("Сгенерировать")
winner = QLabel('?')
#привязка элементов к вертикальной линии
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
main_win.setLayout(line)

#обработка событий
def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText("Побидитель:")

main_win.show()
main_win.setWindowTitle('Генератор')

button.clicked.connect(show_winner)
#запуск приложения

app.exec_()
