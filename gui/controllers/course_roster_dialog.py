import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from gui.CourseRosterDialog import Ui_CourseRosterDialog
from server import Database


class CourseRosterDialog(QtWidgets.QDialog, Ui_CourseRosterDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(CourseRosterDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        rx = QtCore.QRegExp("[^`~!#$%\^&*()+={}\[\]:;\"'<>?/,|\\\\]{,30}")
        validator = QtGui.QRegExpValidator(rx)
        self.searchbar.setValidator(validator)

        self.subject = ""
        self.catalog = ""
        self.section = ""

        self.init_ui()

    def init_ui(self):
        self.searchbar.setFocus()
        self.searchByComboBox.currentIndexChanged.connect(self.update_searchbar)
        self.searchbar.returnPressed.connect(self.handle_search)
        self.closeButton.clicked.connect(self.close_button_clicked)
        self.refreshButton.clicked.connect(self.fill_in)

    def close_button_clicked(self):
        self.close()

    def set_course(self, subject, catalog, section):
        self.subject = subject
        self.catalog = catalog
        self.section = section

    def fill_in(self):
        self.courseNameLabel.setText(self.subject + " " + self.catalog + " - " + self.section)

        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderItem(0, QtGui.QStandardItem("Empl ID"))
        model.setHorizontalHeaderItem(1, QtGui.QStandardItem("Last Name"))
        model.setHorizontalHeaderItem(2, QtGui.QStandardItem("First Name"))

        students = Database.get_class_roster(self.subject, self.catalog, self.section)
        count = 0
        for stud in students["class_roster"]:
            self.studentsTable.setRowCount(count + 1)
            self.studentsTable.setItem(count, 0, QtWidgets.QTableWidgetItem(stud["student_eid"]))
            self.studentsTable.setItem(count, 1, QtWidgets.QTableWidgetItem(stud["student_last_name"]))
            self.studentsTable.setItem(count, 2, QtWidgets.QTableWidgetItem(stud["student_first_name"]))
            model.setItem(count, 0, QtGui.QStandardItem(stud["student_eid"]))
            model.setItem(count, 1, QtGui.QStandardItem(stud["student_last_name"]))
            model.setItem(count, 2, QtGui.QStandardItem(stud["student_first_name"]))
            count += 1

        self.numStudentsLabel.setText(str(self.studentsTable.rowCount()))

        completer = QtWidgets.QCompleter()
        completer.setFilterMode(QtCore.Qt.MatchContains)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer.setModel(model)
        completer.setPopup(QtWidgets.QTableView())
        completer.popup().setMinimumHeight(230)
        self.searchbar.setCompleter(completer)
        self.searchbar.completer().activated[QtCore.QModelIndex].connect(self.handle_activated)

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

    window = CourseRosterDialog()
    window.show()
    app.exec()
