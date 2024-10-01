# -*- coding: utf-8 -*-
# написать программу, использующую QTableView и класс производный от QAbstractTableModel для
# формирования таблицы умножения. достаточно небольшой таблички, 10x10. Достоинством программы
# считается "расцвечивание" ячеек (цветом, начертанием шрифта, выравниванием) в зависимости от
# свойств чисел - чётности, величины остатка деления на некоторое число и т.п.
from PyQt4 import QtCore, QtGui
import sys


# Модель для отображения таблицы умножения
class MultiplicationTableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super(MultiplicationTableModel, self).__init__(parent)
        self.rows = 10
        self.columns = 10

    def rowCount(self, parent=None):
        return self.rows

    def columnCount(self, parent=None):
        return self.columns

    def data(self, index, role):
        if not index.isValid():
            return None

        # Получаем значение для ячейки (таблица умножения)
        row = index.row() + 1
        column = index.column() + 1
        value = row * column

        # Отображение данных в ячейке
        if role == QtCore.Qt.DisplayRole:
            return value

        # Раскрашивание ячеек в зависимости от четности числа
        if role == QtCore.Qt.BackgroundRole:
            if value % 2 == 0:
                return QtGui.QColor("#ADD8E6")  # Светло-синий для четных чисел
            else:
                return QtGui.QColor("#FFB6C1")  # Светло-розовый для нечетных чисел

        # Изменение шрифта для чисел, кратных 5
        if role == QtCore.Qt.FontRole:
            font = QtGui.QFont()
            if value % 5 == 0:
                font.setBold(True)
            return font

        # Выравнивание текста в центре ячейки
        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignCenter

        return None


# Класс основного окна приложения
class MultiplicationTableApp(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MultiplicationTableApp, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # Создаем таблицу и устанавливаем модель
        self.tableView = QtGui.QTableView()
        self.model = MultiplicationTableModel()
        self.tableView.setModel(self.model)

        # Настраиваем компоновку
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)

        self.setWindowTitle('Таблица умножения 10x10')
        self.resize(400, 300)


# Запуск приложения
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MultiplicationTableApp()
    window.show()
    sys.exit(app.exec_())
