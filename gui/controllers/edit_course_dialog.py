import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from gui.EditCourseDialog import Ui_EditCourseDialog
from server import Database


class EditCourseDialog(QtWidgets.QDialog, Ui_EditCourseDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(EditCourseDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        rx = QtCore.QRegExp("[a-zA-Z ]{,30}")
        validator = QtGui.QRegExpValidator(rx)
        self.newSubjectInput.setValidator(validator)

        rx = QtCore.QRegExp("[a-zA-Z0-9]{,7}")
        validator = QtGui.QRegExpValidator(rx)
        self.newCatalogInput.setValidator(validator)
        self.newSectionInput.setValidator(validator)

        rx = QtCore.QRegExp("[a-zA-Z0-9+_.-@]{,30}")
        validator = QtGui.QRegExpValidator(rx)
        self.newProfessorDropDown.setValidator(validator)

        self.prof_last = ""
        self.prof_first = ""
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
        self.newProfessorDropDown.setCompleter(completer)
        self.newProfessorDropDown.setModel(model)
        self.newProfessorDropDown.setView(QtWidgets.QTableView())

        self.cancelButton.clicked.connect(self.cancel_button_clicked)
        self.okButton.clicked.connect(self.ok_button_clicked)
        self.newProfessorDropDown.activated.connect(self.dropdown_activated)
        self.newProfessorDropDown.completer().activated[QtCore.QModelIndex].connect(self.completer_activated)
        self.newSubjectInput.textEdited.connect(self.edit_subject_text)
        self.newCatalogInput.textEdited.connect(self.edit_catalog_text)
        self.newSectionInput.textEdited.connect(self.edit_section_text)

    def cancel_button_clicked(self):
        self.reject()

    def fill_in(self, subject, catalog, section, professor, col):
        self.ogSubjectInput.setText(subject)
        self.newSubjectInput.setText(subject)
        self.ogCatalogInput.setText(catalog)
        self.newCatalogInput.setText(catalog)
        self.ogSectionInput.setText(section)
        self.newSectionInput.setText(section)
        self.ogProfessorInput.setText(professor)

        if col == 0:
            self.newSubjectInput.setFocus()
        elif col == 1:
            self.newCatalogInput.setFocus()
        elif col == 2:
            self.newSectionInput.setFocus()
        else:
            self.newProfessorDropDown.setFocus()

    def ok_button_clicked(self):
        professor = {"first_name": self.prof_first, "last_name": self.prof_last, "email": self.prof_email}
        course = {"subject": self.newSubjectInput.text(), "catalog": self.newCatalogInput.text(),
                  "section": self.newSectionInput.text(), "professor": professor}
        old_course = {"subject": self.ogSubjectInput.text(), "catalog": self.ogCatalogInput.text(),
                      "section": self.ogSectionInput.text()}
        result = Database.update_class(old_course, course)
        if result is True:
            self.accept()
        else:
            print("couldn't update course")

    def dropdown_activated(self, index):
        self.prof_last = self.newProfessorDropDown.model().item(index, 0).text()
        self.prof_first = self.newProfessorDropDown.model().item(index, 1).text()
        self.prof_email = self.newProfessorDropDown.model().item(index, 2).text()
        self.set_dropdown_text()

    def completer_activated(self, index):
        self.prof_last = index.sibling(index.row(), 0).data()
        self.prof_first = index.sibling(index.row(), 1).data()
        self.prof_email = index.sibling(index.row(), 2).data()
        QtCore.QTimer.singleShot(2, self.set_dropdown_text)

    def set_dropdown_text(self):
        self.newProfessorDropDown.setCurrentText(self.prof_first + " " + self.prof_last + ", " + self.prof_email)

    def edit_subject_text(self, text):
        self.newSubjectInput.setText(text.upper())

    def edit_catalog_text(self, text):
        self.newCatalogInput.setText(text.upper())

    def edit_section_text(self, text):
        self.newSectionInput.setText(text.upper())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = EditCourseDialog()
    window.show()
    app.exec()
