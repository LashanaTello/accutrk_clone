import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from gui.StudentsPage import Ui_StudentsPage
from server import Database


class StudentsPage(QtWidgets.QDialog, Ui_StudentsPage):
    def __init__(self, *args, obj=None, **kwargs):
        super(StudentsPage, self).__init__(*args, **kwargs)
        self.setupUi(self)

        rx = QtCore.QRegExp("[^`~!#$%\^&*()+={}\[\]:;\"'<>?/,|\\\\]{30}")
        validator = QtGui.QRegExpValidator(rx)
        self.searchbar.setValidator(validator)

        self.init_ui()

    def init_ui(self):
        self.closeButton.clicked.connect(self.close_button_clicked)
        self.searchByComboBox.setPlaceholderText("Search by...")

        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderItem(0, QtGui.QStandardItem("Empl ID"))
        model.setHorizontalHeaderItem(1, QtGui.QStandardItem("Last Name"))
        model.setHorizontalHeaderItem(2, QtGui.QStandardItem("First Name"))
        model.setHorizontalHeaderItem(3, QtGui.QStandardItem("Barcode"))
        model.setHorizontalHeaderItem(4, QtGui.QStandardItem("Email"))


        students = Database.get_all_students()
        count = 0
        for student in students:
            self.studentsTable.setRowCount(count + 1)
            self.studentsTable.setItem(count, 0, QtWidgets.QTableWidgetItem(student["eid"]))
            self.studentsTable.setItem(count, 1, QtWidgets.QTableWidgetItem(student["last_name"]))
            self.studentsTable.setItem(count, 2, QtWidgets.QTableWidgetItem(student["first_name"]))
            self.studentsTable.setItem(count, 3, QtWidgets.QTableWidgetItem(student["barcode"]))
            self.studentsTable.setItem(count, 4, QtWidgets.QTableWidgetItem(student["email"]))

            model.setItem(count, 0, QtGui.QStandardItem(student["eid"]))
            model.setItem(count, 1, QtGui.QStandardItem(student["last_name"]))
            model.setItem(count, 2, QtGui.QStandardItem(student["first_name"]))
            model.setItem(count, 3, QtGui.QStandardItem(student["barcode"]))
            model.setItem(count, 4, QtGui.QStandardItem(student["email"]))
            count += 1

        completer = QtWidgets.QCompleter()
        completer.setFilterMode(QtCore.Qt.MatchContains)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer.setModel(model)
        self.searchbar.setCompleter(completer)

        self.numStudentsLabel.setText(str(self.studentsTable.rowCount()))
        self.searchByComboBox.setFocus()

    def close_button_clicked(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = StudentsPage()
    window.show()
    app.exec()
