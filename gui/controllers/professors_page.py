import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from gui.ProfessorsPage import Ui_ProfessorsPage
from gui.controllers.edit_dialog import EditDialog
from gui.controllers.add_student_dialog import AddStudentDialog
from gui.controllers.delete_student_dialog import DeleteStudentDialog
from server import Database


class ProfessorsPage(QtWidgets.QDialog, Ui_ProfessorsPage):
    def __init__(self, *args, obj=None, **kwargs):
        super(ProfessorsPage, self).__init__(*args, **kwargs)
        self.setupUi(self)

        rx = QtCore.QRegExp("[^`~!#$%\^&*()+={}\[\]:;\"'<>?/,|\\\\]{,30}")
        validator = QtGui.QRegExpValidator(rx)
        self.searchbar.setValidator(validator)

        self.edit_dialog = None
        self.add_dialog = None
        self.delete_dialog = None

        self.init_ui()

    def init_ui(self):
        self.closeButton.clicked.connect(self.close_button_clicked)
        self.searchByComboBox.setPlaceholderText("Search by...")
        self.searchbar.setPlaceholderText("Search by Last Name...")

        self.fill_table()
        self.searchbar.setFocus()

        self.searchByComboBox.currentIndexChanged.connect(self.update_searchbar)
        self.searchbar.returnPressed.connect(self.handle_search)
        self.searchbar.completer().activated[QtCore.QModelIndex].connect(self.handle_activated)
        self.editButton.clicked.connect(self.edit_button_clicked)
        self.refreshButton.clicked.connect(self.fill_table)
        self.addButton.clicked.connect(self.add_button_clicked)
        self.deleteButton.clicked.connect(self.delete_button_clicked)

    def close_button_clicked(self):
        self.close()

    def update_searchbar(self, index):
        self.searchbar.setPlaceholderText("Search by " + self.searchByComboBox.currentText() + "...")
        self.searchbar.completer().setCompletionColumn(index)

    def handle_activated(self, index):
        match = self.professorsTable.findItems(index.sibling(index.row(), 0).data(), QtCore.Qt.MatchExactly)
        self.professorsTable.selectRow(match[0].row())
        self.professorsTable.scrollToItem(self.professorsTable.item(match[0].row(), 0))

    def handle_search(self):
        match = self.professorsTable.findItems(self.searchbar.text(), QtCore.Qt.MatchExactly)
        if len(match) == 0:
            return
        else:
            self.professorsTable.selectRow(match[0].row())
            self.professorsTable.scrollToItem(self.professorsTable.item(match[0].row(), 0))

    def edit_button_clicked(self):
        row = self.professorsTable.currentRow()
        if row < 0:
            print("select a cell or row")
        else:
            self.edit_dialog = EditDialog()
            self.edit_dialog.fill_in_professor(self.professorsTable.item(row, 0).text(),
                                               self.professorsTable.item(row, 1).text(),
                                               self.professorsTable.item(row, 2).text(),
                                               self.professorsTable.currentColumn())
            self.edit_dialog.open()
            self.edit_dialog.finished.connect(self.evaluate)

    def evaluate(self, result):
        if result is 1:
            self.fill_table()

    def add_button_clicked(self):
        self.add_dialog = AddStudentDialog()
        self.add_dialog.adjust_display()
        self.add_dialog.open()
        self.add_dialog.finished.connect(self.evaluate)

    def delete_button_clicked(self):
        row = self.professorsTable.currentRow()
        if row < 0:
            print("select a cell or row")
        else:
            self.delete_dialog = DeleteStudentDialog()
            self.delete_dialog.fill_in_prof(self.professorsTable.item(row, 1).text(),
                                            self.professorsTable.item(row, 0).text(),
                                            self.professorsTable.item(row, 2).text())
            self.delete_dialog.open()
            self.delete_dialog.finished.connect(self.evaluate)

    def fill_table(self):
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderItem(0, QtGui.QStandardItem("Last Name"))
        model.setHorizontalHeaderItem(1, QtGui.QStandardItem("First Name"))
        model.setHorizontalHeaderItem(2, QtGui.QStandardItem("Email"))

        profs = Database.get_all_professors()
        count = 0
        for prof in profs:
            self.professorsTable.setRowCount(count + 1)
            self.professorsTable.setItem(count, 0, QtWidgets.QTableWidgetItem(prof["last_name"]))
            self.professorsTable.setItem(count, 1, QtWidgets.QTableWidgetItem(prof["first_name"]))
            self.professorsTable.setItem(count, 2, QtWidgets.QTableWidgetItem(prof["email"]))

            model.setItem(count, 0, QtGui.QStandardItem(prof["last_name"]))
            model.setItem(count, 1, QtGui.QStandardItem(prof["first_name"]))
            model.setItem(count, 2, QtGui.QStandardItem(prof["email"]))
            count += 1

        self.numProfessorsLabel.setText(str(self.professorsTable.rowCount()))

        completer = QtWidgets.QCompleter()
        completer.setFilterMode(QtCore.Qt.MatchContains)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer.setModel(model)
        popup = QtWidgets.QTableView()
        popup.setModel(model)
        popup.setMinimumWidth(530)
        popup.setMinimumHeight(250)
        popup.setColumnWidth(0, 150)
        popup.setColumnWidth(1, 150)
        popup.setColumnWidth(2, 215)
        completer.setPopup(popup)
        self.searchbar.setCompleter(completer)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = ProfessorsPage()
    window.show()
    app.exec()
