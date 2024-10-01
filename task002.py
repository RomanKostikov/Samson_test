# -*- coding: utf-8 -*-
# Необходимо создать графическое приложение с формой для ввода исходной строки и вывода
# перевёрнутой, используя функцию из задания 1.
from PyQt4 import QtGui
import sys


# Функция для переворачивания строки из задания 1
def reverse_string(s):
    return s[::-1]


# Основной класс приложения
class ReverseStringApp(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ReverseStringApp, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # Создаем элементы интерфейса
        self.input_label = QtGui.QLabel('Введите строку:')
        self.input_text = QtGui.QLineEdit()
        self.reverse_button = QtGui.QPushButton('Перевернуть')
        self.output_label = QtGui.QLabel('Перевёрнутая строка:')
        self.output_text = QtGui.QLineEdit()
        self.output_text.setReadOnly(True)

        # Устанавливаем компоновку
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_text)
        layout.addWidget(self.reverse_button)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_text)
        self.setLayout(layout)

        # Подключаем сигнал к слоту
        self.reverse_button.clicked.connect(self.reverseInputString)

        self.setWindowTitle('Переворачивание строки')
        self.resize(300, 150)

    def reverseInputString(self):
        original_string = self.input_text.text()
        reversed_string = reverse_string(unicode(original_string))
        self.output_text.setText(reversed_string)


# Запуск приложения
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = ReverseStringApp()
    window.show()
    sys.exit(app.exec_())
