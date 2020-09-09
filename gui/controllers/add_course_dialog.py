import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from gui.AddCourseDialog import Ui_addCourseDialog
from server import Database


class AddCourseDialog(QtWidgets.QDialog, Ui_addCourseDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(AddCourseDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        rx = QtCore.QRegExp("[a-zA-Z ]{,30}")
        validator = QtGui.QRegExpValidator(rx)
        self.subjectInput.setValidator(validator)

        rx = QtCore.QRegExp("[a-zA-Z0-9]{,7}")
        validator = QtGui.QRegExpValidator(rx)
        self.catalogInput.setValidator(validator)
        self.sectionInput.setValidator(validator)

        rx = QtCore.QRegExp("[a-zA-Z0-9+_.-@]{,30}")
        validator = QtGui.QRegExpValidator(rx)
        self.professorDropDown.setValidator(validator)

        self.prof_first = ""
        self.prof_last = ""
        self.prof_email = ""

        self.init_ui()

    def init_ui(self):
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderItem(0, QtGui.QStandardItem("Last Name"))
        model.setHorizontalHeaderItem(1, QtGui.QStandardItem("First Name"))
        model.setHorizontalHeaderItem(2, QtGui.QStandardItem("Email"))

        profs = Database.get_all_professors()
        count = 0
        for prof in profs:
            model.setItem(count, 0, QtGui.QStandardItem(prof["last_name"]))
            model.setItem(count, 1, QtGui.QStandardItem(prof["first_name"]))
            model.setItem(count, 2, QtGui.QStandardItem(prof["email"]))
            count += 1

        completer = QtWidgets.QCompleter()
        completer.setFilterMode(QtCore.Qt.MatchContains)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer.setModel(model)
        popup = QtWidgets.QTableView()
        popup.setModel(model)
        popup.setMinimumSize(320, 250)
        completer.setPopup(popup)
        self.professorDropDown.setCompleter(completer)
        self.professorDropDown.setModel(model)
        self.professorDropDown.setView(QtWidgets.QTableView())

        self.cancelButton.clicked.connect(self.cancel_button_clicked)
        self.addButton.clicked.connect(self.add_button_clicked)
        self.professorDropDown.activated.connect(self.dropdown_activated)
        self.professorDropDown.completer().activated[QtCore.QModelIndex].connect(self.completer_activated)
        self.subjectInput.textEdited.connect(self.edit_text)

    def cancel_button_clicked(self):
        self.reject()

    def add_button_clicked(self):
        professor = {"first_name": self.prof_first, "last_name": self.prof_last, "email": self.prof_email}
        result = Database.add_class(self.subjectInput.text(), self.catalogInput.text(), self.sectionInput.text(),
                                    professor)
        if result is True:
            self.accept()
        else:
            print("could not add course")

    def dropdown_activated(self, index):
        self.prof_last = self.professorDropDown.model().item(index, 0).text()
        self.prof_first = self.professorDropDown.model().item(index, 1).text()
        self.prof_email = self.professorDropDown.model().item(index, 2).text()
        self.set_dropdown_text()

    def completer_activated(self, index):
        self.prof_last = index.sibling(index.row(), 0).data()
        self.prof_first = index.sibling(index.row(), 1).data()
        self.prof_email = index.sibling(index.row(), 2).data()
        QtCore.QTimer.singleShot(2, self.set_dropdown_text)

    def set_dropdown_text(self):
        self.professorDropDown.setCurrentText(self.prof_first + " " + self.prof_last + ", " + self.prof_email)

    def edit_text(self, text):
        self.subjectInput.setText(text.upper())

    # def validate_input(self):
    #     valid = []
    #     if not self.EIDInput.hasAcceptableInput():
    #         valid.append(0)
    #     if not self.barcodeInput.hasAcceptableInput():
    #         valid.append(1)
    #     if not self.firstNameInput.hasAcceptableInput():
    #         valid.append(2)
    #     if not self.lastNameInput.hasAcceptableInput():
    #         valid.append(3)
    #     if not self.emailInput.hasAcceptableInput():
    #         valid.append(4)
    #
    #     if len(valid) == 0:
    #         return True
    #     return valid


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = AddCourseDialog()
    window.show()
    app.exec()
