import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sqlite3


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем дизайн

        self.comboBox.addItem('Ристретто')
        self.comboBox.addItem('Капучино')
        self.comboBox.addItem('Американо')
        self.comboBox.addItem('Экспрессо')

        self.pushButton.clicked.connect(self.run)

        self.LE_1.setEnabled(False)
        self.LE_2.setEnabled(False)
        self.LE_3.setEnabled(False)
        self.LE_4.setEnabled(False)
        self.LE_5.setEnabled(False)
        self.LE_6.setEnabled(False)
        self.LE_7.setEnabled(False)

    def run(self):
        try:
            text = self.comboBox.currentText()
            text = text.lower()

            connect = sqlite3.connect('coffee.sqlite')
            cursor = connect.cursor()

            result = cursor.execute("""
            SELECT * FROM coffes
            WHERE title = ?
            """, (text, )).fetchall()[0]

            id = str(result[0]).title()
            title = str(result[1]).title()
            degree = str(result[2]).title()
            type = str(result[3]).title()
            description = str(result[4])
            price = str(result[5]).title()
            volume = str(result[6]).title()

            self.LE_1.setText(str(id))
            self.LE_2.setText(str(title))
            self.LE_3.setText(str(degree))
            self.LE_4.setText(str(type))
            self.LE_5.setText(str(description))
            self.LE_6.setText(str(price))
            self.LE_7.setText(str(volume))
        except Exception as e:
            print(e)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec())
