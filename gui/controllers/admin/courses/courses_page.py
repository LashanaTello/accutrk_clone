import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from gui.CoursesPage import Ui_CoursesPage
from gui.controllers.admin.courses.edit_course_dialog import EditCourseDialog
from gui.controllers.admin.courses.add_course_dialog import AddCourseDialog
from gui.controllers.admin.delete_dialog import DeleteDialog
from gui.controllers.admin.courses.course_roster_dialog import CourseRosterDialog
from server import Database


class CoursesPage(QtWidgets.QDialog, Ui_CoursesPage):
    def __init__(self, *args, obj=None, **kwargs):
        super(CoursesPage, self).__init__(*args, **kwargs)
        self.setupUi(self)

        rx = QtCore.QRegExp("[^`~!#$%\^&*()+={}\[\]:;\"'<>?/,|\\\\]{,30}")
        validator = QtGui.QRegExpValidator(rx)
        self.searchbar.setValidator(validator)

        self.edit_dialog = None
        self.add_dialog = None
        self.delete_dialog = None
        self.course_roster_dialog = None

        self.init_ui()

    def init_ui(self):
        self.closeButton.clicked.connect(self.close_button_clicked)
        self.searchByComboBox.setPlaceholderText("Search by...")
        self.searchbar.setPlaceholderText("Search by Subject...")

        self.fill_table()
        self.searchbar.setFocus()

        self.searchByComboBox.currentIndexChanged.connect(self.update_searchbar)
        self.searchbar.returnPressed.connect(self.handle_search)
        self.searchbar.completer().activated[QtCore.QModelIndex].connect(self.handle_activated)
        self.editButton.clicked.connect(self.edit_button_clicked)
        self.refreshButton.clicked.connect(self.fill_table)
        self.addButton.clicked.connect(self.add_button_clicked)
        self.deleteButton.clicked.connect(self.delete_button_clicked)
        self.registrationButton.clicked.connect(self.registration_button_clicked)

    def close_button_clicked(self):
        self.close()

    def update_searchbar(self, index):
        self.searchbar.setPlaceholderText("Search by " + self.searchByComboBox.currentText() + "...")
        self.searchbar.completer().setCompletionColumn(index)

    def handle_activated(self, index):
        match = self.coursesTable.findItems(index.sibling(index.row(), 6).data(), QtCore.Qt.MatchExactly)
        self.coursesTable.selectRow(match[0].row())
        self.coursesTable.scrollToItem(self.coursesTable.item(match[0].row(), 0))

    def handle_search(self):
        match = self.coursesTable.findItems(self.searchbar.text(), QtCore.Qt.MatchExactly)
        if len(match) == 0:
            return
        else:
            self.coursesTable.selectRow(match[0].row())
            self.coursesTable.scrollToItem(self.coursesTable.item(match[0].row(), 0))

    def edit_button_clicked(self):
        row = self.coursesTable.currentRow()
        if row < 0:
            print("select a cell or row")
        else:
            self.edit_dialog = EditCourseDialog()
            self.edit_dialog.fill_in(self.coursesTable.item(row, 0).text(), self.coursesTable.item(row, 1).text(),
                                     self.coursesTable.item(row, 2).text(), self.coursesTable.item(row, 4).text(),
                                     self.coursesTable.currentColumn())
            self.edit_dialog.open()
            self.edit_dialog.finished.connect(self.evaluate)

    def evaluate(self, result):
        if result is 1:
            self.fill_table()

    def add_button_clicked(self):
        self.add_dialog = AddCourseDialog()
        self.add_dialog.open()
        self.add_dialog.finished.connect(self.evaluate)

    def delete_button_clicked(self):
        row = self.coursesTable.currentRow()
        if row < 0:
            print("select a cell or row")
        else:
            self.delete_dialog = DeleteDialog()
            self.delete_dialog.fill_in_course(self.coursesTable.item(row, 0).text(),
                                              self.coursesTable.item(row, 1).text(),
                                              self.coursesTable.item(row, 2).text())
            self.delete_dialog.open()
            self.delete_dialog.finished.connect(self.evaluate)

    def registration_button_clicked(self):
        row = self.coursesTable.currentRow()
        if row < 0:
            print("select a cell or row")
        else:
            self.course_roster_dialog = CourseRosterDialog()
            self.course_roster_dialog.set_course(self.coursesTable.item(row, 0).text(),
                                                 self.coursesTable.item(row, 1).text(),
                                                 self.coursesTable.item(row, 2).text())
            self.course_roster_dialog.fill_in()
            self.course_roster_dialog.open()

    def fill_table(self):
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderItem(0, QtGui.QStandardItem("Subject"))
        model.setHorizontalHeaderItem(1, QtGui.QStandardItem("Catalog"))
        model.setHorizontalHeaderItem(2, QtGui.QStandardItem("Section"))
        model.setHorizontalHeaderItem(3, QtGui.QStandardItem("# of Students"))
        model.setHorizontalHeaderItem(4, QtGui.QStandardItem("Professor"))
        model.setHorizontalHeaderItem(5, QtGui.QStandardItem("Professor Email"))
        model.setHorizontalHeaderItem(6, QtGui.QStandardItem("UniqueIndex"))

        courses = Database.get_classes_with_size()
        count = 0
        for course in courses:
            self.coursesTable.setRowCount(count + 1)
            self.coursesTable.setItem(count, 0, QtWidgets.QTableWidgetItem(course["subject"]))
            self.coursesTable.setItem(count, 1, QtWidgets.QTableWidgetItem(course["catalog"]))
            self.coursesTable.setItem(count, 2, QtWidgets.QTableWidgetItem(course["section"]))
            self.coursesTable.setItem(count, 3, QtWidgets.QTableWidgetItem(str(course["count"])))
            if course["professor"] != {}:
                self.coursesTable.setItem(count, 4, QtWidgets.QTableWidgetItem(course["professor"]["first_name"] + " " +
                                                                               course["professor"]["last_name"]))
                self.coursesTable.setItem(count, 5, QtWidgets.QTableWidgetItem(course["professor"]["email"]))
            else:
                self.coursesTable.setItem(count, 4, QtWidgets.QTableWidgetItem(""))
                self.coursesTable.setItem(count, 5, QtWidgets.QTableWidgetItem(""))
            self.coursesTable.setItem(count, 6, QtWidgets.QTableWidgetItem(course["subject"] + course["catalog"] +
                                                                           course["section"]))

            model.setItem(count, 0, QtGui.QStandardItem(course["subject"]))
            model.setItem(count, 1, QtGui.QStandardItem(course["catalog"]))
            model.setItem(count, 2, QtGui.QStandardItem(course["section"]))
            model.setItem(count, 3, QtGui.QStandardItem(str(course["count"])))
            if course["professor"] != {}:
                model.setItem(count, 4, QtGui.QStandardItem(course["professor"]["first_name"] + " " +
                                                            course["professor"]["last_name"]))
                model.setItem(count, 5, QtGui.QStandardItem(course["professor"]["email"]))
            else:
                model.setItem(count, 4, QtGui.QStandardItem(""))
                model.setItem(count, 5, QtGui.QStandardItem(""))
            model.setItem(count, 6, QtGui.QStandardItem(course["subject"] + course["catalog"] + course["section"]))
            count += 1

        self.coursesTable.setColumnHidden(6, True)
        self.numCoursesLabel.setText(str(self.coursesTable.rowCount()))

        completer = QtWidgets.QCompleter()
        completer.setFilterMode(QtCore.Qt.MatchContains)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer.setModel(model)
        popup = QtWidgets.QTableView()
        popup.setModel(model)
        popup.setColumnHidden(6, True)
        popup.setMinimumWidth(805)
        popup.setMinimumHeight(300)
        popup.setColumnWidth(4, 170)
        popup.setColumnWidth(5, 220)
        completer.setPopup(popup)
        self.searchbar.setCompleter(completer)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = CoursesPage()
    window.show()
    app.exec()
