import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from gui.StudentsPage import Ui_StudentsPage
from server import Database


class StudentsPage(QtWidgets.QDialog, Ui_StudentsPage):
    def __init__(self, *args, obj=None, **kwargs):
        super(StudentsPage, self).__init__(*args, **kwargs)
        self.setupUi(self)

        rx = QtCore.QRegExp("[^`~!#$%\^&*()+={}\[\]:;\"'<>?/,|\\\\]{,30}")
        validator = QtGui.QRegExpValidator(rx)
        self.searchbar.setValidator(validator)

        self.init_ui()

    def init_ui(self):
        self.closeButton.clicked.connect(self.close_button_clicked)
        self.searchByComboBox.setPlaceholderText("Search by...")
        self.searchbar.setPlaceholderText("Search by Empl ID...")

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
        completer.setPopup(QtWidgets.QTableView())
        completer.popup().setMinimumHeight(250)
        self.searchbar.setCompleter(completer)

        self.numStudentsLabel.setText(str(self.studentsTable.rowCount()))
        self.searchbar.setFocus()

        self.searchByComboBox.currentIndexChanged.connect(self.update_searchbar)
        self.searchbar.returnPressed.connect(self.handle_search)
        self.searchbar.completer().activated[QtCore.QModelIndex].connect(self.handle_activated)

    def close_button_clicked(self):
        self.close()

    def update_searchbar(self, index):
        self.searchbar.setPlaceholderText("Search by " + self.searchByComboBox.currentText() + "...")
        self.searchbar.completer().setCompletionColumn(index)

    def handle_activated(self, index):
        match = self.studentsTable.findItems(index.sibling(index.row(), 0).data(), QtCore.Qt.MatchExactly)
        self.studentsTable.selectRow(match[0].row())
        self.studentsTable.scrollToItem(self.studentsTable.item(match[0].row(), 0))

    def handle_search(self):
        match = self.studentsTable.findItems(self.searchbar.text(), QtCore.Qt.MatchExactly)
        if len(match) == 0:
            return
        else:
            self.studentsTable.selectRow(match[0].row())
            self.studentsTable.scrollToItem(self.studentsTable.item(match[0].row(), 0))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = StudentsPage()
    window.show()
    app.exec()
