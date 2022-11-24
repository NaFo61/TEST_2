import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sqlite3
from addEditCoffeeForm import Ui_MainWindow

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.GOG = None

        self.hide()

        self.main_title = None

        connect = sqlite3.connect('C:/Users/NAFO/PycharmProjects/pythonProject/git_hub_yandex/v_3/data/coffee.sqlite')
        cursor = connect.cursor()
        titles = [i[0] for i in cursor.execute("""
        SELECT title FROM coffes
        """).fetchall()]
        self.CB.addItems(titles)

        self.B_create_create.clicked.connect(self.create_)
        self.B_create_save.clicked.connect(self.create_save)
        self.B_edit_edit.clicked.connect(self.edit_)
        self.B_edit_find.clicked.connect(self.edit_find)
        self.B_edit_save.clicked.connect(self.edit_save)

    def hide(self):
        # Закрываем create:
        self.L_1.hide()
        self.L_2.hide()
        self.L_3.hide()
        self.L_4.hide()
        self.L_5.hide()
        self.L_6.hide()
        self.LE_1.hide()
        self.LE_2.hide()
        self.LE_3.hide()
        self.LE_4.hide()
        self.LE_5.hide()
        self.LE_6.hide()
        self.B_create_save.hide()
        # Закрываем edit:
        self.L_7.hide()
        self.L_8.hide()
        self.L_9.hide()
        self.L_10.hide()
        self.L_11.hide()
        self.L_12.hide()
        self.LE_7.hide()
        self.LE_8.hide()
        self.LE_9.hide()
        self.LE_10.hide()
        self.LE_11.hide()
        self.LE_12.hide()
        self.B_edit_find.hide()
        self.B_edit_save.hide()
        self.CB.hide()

    def open_create(self):
        # Открываем create:
        self.L_1.show()
        self.L_2.show()
        self.L_3.show()
        self.L_4.show()
        self.L_5.show()
        self.L_6.show()
        self.LE_1.show()
        self.LE_2.show()
        self.LE_3.show()
        self.LE_4.show()
        self.LE_5.show()
        self.LE_6.show()
        self.B_create_save.show()
        # Закрываем edit:
        self.L_7.hide()
        self.L_8.hide()
        self.L_9.hide()
        self.L_10.hide()
        self.L_11.hide()
        self.L_12.hide()
        self.LE_7.hide()
        self.LE_8.hide()
        self.LE_9.hide()
        self.LE_10.hide()
        self.LE_11.hide()
        self.LE_12.hide()
        self.B_edit_find.hide()
        self.B_edit_save.hide()
        self.CB.hide()
        # Очистка edit:
        self.LE_7.setText('')
        self.LE_8.setText('')
        self.LE_9.setText('')
        self.LE_10.setText('')
        self.LE_11.setText('')
        self.LE_12.setText('')

    def open_edit(self):
        self.GOG = False
        # Открываем edit:
        self.L_7.show()
        self.L_8.show()
        self.L_9.show()
        self.L_10.show()
        self.L_11.show()
        self.L_12.show()
        self.LE_7.show()
        self.LE_8.show()
        self.LE_9.show()
        self.LE_10.show()
        self.LE_11.show()
        self.LE_12.show()
        self.B_edit_find.show()
        self.B_edit_save.show()
        self.CB.show()
        # Закрываем create:
        self.L_1.hide()
        self.L_2.hide()
        self.L_3.hide()
        self.L_4.hide()
        self.L_5.hide()
        self.L_6.hide()
        self.LE_1.hide()
        self.LE_2.hide()
        self.LE_3.hide()
        self.LE_4.hide()
        self.LE_5.hide()
        self.LE_6.hide()
        self.B_create_save.hide()
        # Очистка create:
        self.LE_1.setText('')
        self.LE_2.setText('')
        self.LE_3.setText('')
        self.LE_4.setText('')
        self.LE_5.setText('')
        self.LE_6.setText('')

    def create_(self):
        self.open_create()

    def create_save(self):
        title = self.LE_1.text().lower()
        degree = self.LE_2.text().lower()
        type = self.LE_3.text().lower()
        description = self.LE_4.text().lower()
        price = self.LE_5.text().lower()
        volume = self.LE_6.text().lower()

        if title and degree and type and description and price and volume:

            connect = sqlite3.connect('C:/Users/NAFO/PycharmProjects/pythonProject/git_hub_yandex/v_3/data/coffee.sqlite')
            cursor = connect.cursor()

            titles = [i[0] for i in cursor.execute("""
            SELECT title FROM coffes
            """).fetchall()]
            if title not in titles:
                cursor.execute("""
                INSERT INTO coffes(title, degree, type, description, price, volume) VALUES(?, ?, ?, ?, ?, ?)
                """, (title, degree, type, description, price, volume))
                connect.commit()
                connect.close()
            else:
                print('Ошибка, одинаковое название')
        else:
            print('Ошибка, не веденны все значения')

    def edit_(self):
        self.open_edit()

    def edit_find(self):
        self.GOG = True
        connect = sqlite3.connect('C:/Users/NAFO/PycharmProjects/pythonProject/git_hub_yandex/v_3/data/coffee.sqlite')
        cursor = connect.cursor()

        self.main_title = self.CB.currentText()

        result = [i for i in cursor.execute("""
        SELECT title, degree, type, description, price, volume FROM coffes
        WHERE title = ?
        """, (self.main_title,)).fetchall()[0]]

        title = str(result[0]).title()
        degree = str(result[1]).title()
        type = str(result[2]).title()
        description = str(result[3])
        price = str(result[4]).title()
        volume = str(result[5]).title()

        self.LE_7.setText(str(title))
        self.LE_8.setText(str(degree))
        self.LE_9.setText(str(type))
        self.LE_10.setText(str(description))
        self.LE_11.setText(str(price))
        self.LE_12.setText(str(volume))

    def edit_save(self):
        try:
            if self.GOG:
                title = self.LE_7.text().lower()
                degree = self.LE_8.text().lower()
                type = self.LE_9.text().lower()
                description = self.LE_10.text().lower()
                price = self.LE_11.text().lower()
                volume = self.LE_12.text().lower()

                connect = sqlite3.connect('C:/Users/NAFO/PycharmProjects/pythonProject/git_hub_yandex/v_3/data/coffee.sqlite')
                cursor = connect.cursor()

                id = cursor.execute("""
                SELECT id FROM coffes
                WHERE title = ?
                """, (self.main_title,)).fetchone()[0]

                cursor.execute("""
                UPDATE coffes
                SET title = ?
                WHERE id = ?
                """, (title, id))

                cursor.execute("""
                UPDATE coffes
                SET degree = ?
                WHERE id = ?
                """, (degree, id))

                cursor.execute("""
                UPDATE coffes
                SET type = ?
                WHERE id = ?
                """, (type, id))

                cursor.execute("""
                UPDATE coffes
                SET description = ?
                WHERE id = ?
                """, (description, id))

                cursor.execute("""
                UPDATE coffes
                SET price = ?
                WHERE id = ?
                """, (price, id))

                cursor.execute("""
                UPDATE coffes
                SET volume = ?
                WHERE id = ?
                """, (volume, id))

                connect.commit()
                connect.close()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec())
