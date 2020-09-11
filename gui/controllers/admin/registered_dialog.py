import sys
from PyQt5 import QtWidgets

from gui.RegisteredDialog import Ui_RegisteredDialog
from gui.helperfunctions.helpers import convert_time
from server import Database


class RegisteredDialog(QtWidgets.QDialog, Ui_RegisteredDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(RegisteredDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.init_ui()

    def init_ui(self):
        self.doneButton.clicked.connect(self.done_button_clicked)

    def done_button_clicked(self):
        self.close()

    def fill_in(self, student_id, first, last):
        self.EIDInput.setText(student_id)
        self.firstNameInput.setText(first)
        self.lastNameInput.setText(last)

        classes = Database.get_student_classes(student_id)
        count = 0
        for a_class in classes["enrolled_list"]:
            self.classesTable.setRowCount(count + 1)
            self.classesTable.setItem(count, 0, QtWidgets.QTableWidgetItem(a_class["subject"]))
            self.classesTable.setItem(count, 1, QtWidgets.QTableWidgetItem(a_class["catalog"]))
            self.classesTable.setItem(count, 2, QtWidgets.QTableWidgetItem(a_class["section"]))
            # this has to be changed
            self.classesTable.setItem(count, 3, QtWidgets.QTableWidgetItem((a_class["registered_by"])))
            self.classesTable.setItem(count, 4, QtWidgets.QTableWidgetItem(a_class["registered_date"]))
            count += 1


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = RegisteredDialog()
    window.show()
    app.exec()
