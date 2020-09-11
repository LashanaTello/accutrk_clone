import sys
from PyQt5 import QtWidgets

from gui.CheckedInListPage import Ui_CheckedInList
from server import Database
from gui.helperfunctions.helpers import convert_time, combine_into_class


class CheckedInListPage(QtWidgets.QDialog, Ui_CheckedInList):
    def __init__(self, *args, obj=None, **kwargs):
        super(CheckedInListPage, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.checked_in_list = []

        self.init_ui()

    def init_ui(self):
        self.closeWindowButton.clicked.connect(self.close_button_clicked)
        self.checked_in_list = Database.get_current_logins()
        self.loginList.setRowCount(self.checked_in_list.count())
        self.numberOfStudents.setText(str(self.checked_in_list.count()))
        count = 0
        for student in self.checked_in_list:
            self.loginList.setItem(count, 0, QtWidgets.QTableWidgetItem(student["last_name"]))
            self.loginList.setItem(count, 1, QtWidgets.QTableWidgetItem(student["first_name"]))
            self.loginList.setItem(count, 2, QtWidgets.QTableWidgetItem(convert_time(student["login_time"])))
            self.loginList.setItem(count, 3, QtWidgets.QTableWidgetItem(student["logout_time"]))
            a_class = combine_into_class(student["subject"], student["catalog"], student["section"])
            self.loginList.setItem(count, 4, QtWidgets.QTableWidgetItem(a_class))
            self.loginList.setItem(count, 5, QtWidgets.QTableWidgetItem(student["service"]))
            count += 1

        self.loginList.sortItems(0)

    def close_button_clicked(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = CheckedInListPage()
    window.show()
    app.exec()
