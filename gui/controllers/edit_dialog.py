import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from gui.EditDialog import Ui_EditDialog
from server import Database


class EditDialog(QtWidgets.QDialog, Ui_EditDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(EditDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        rx = QtCore.QRegExp("[0-9]{8}")
        validator = QtGui.QRegExpValidator(rx)
        self.newEIDInput.setValidator(validator)

        rx = QtCore.QRegExp("[0-9]{14}")
        validator = QtGui.QRegExpValidator(rx)
        self.newBarcodeInput.setValidator(validator)

        rx = QtCore.QRegExp("[-a-zA-Z ]{25}")
        validator = QtGui.QRegExpValidator(rx)
        self.newLastNameInput.setValidator(validator)
        self.newFirstNameInput.setValidator(validator)

        rx = QtCore.QRegExp("^[a-z0-9+_.-]+@[a-z0-9.-]+$")
        validator = QtGui.QRegExpValidator(rx)
        self.newEmailInput.setValidator(validator)

        self.init_ui()

    def init_ui(self):
        self.cancelButton.clicked.connect(self.cancel_button_clicked)
        self.okButton.clicked.connect(self.ok_button_clicked)

    def cancel_button_clicked(self):
        self.reject()

    def fill_in(self, eid, last, first, barcode, email, col):
        self.ogEIDInput.setText(eid)
        self.newEIDInput.setText(eid)
        self.ogBarcodeInput.setText(barcode)
        self.newBarcodeInput.setText(barcode)
        self.ogLastNameInput.setText(last)
        self.newLastNameInput.setText(last)
        self.ogFirstNameInput.setText(first)
        self.newFirstNameInput.setText(first)
        self.ogEmailInput.setText(email)
        self.newEmailInput.setText(email)

        if col == 0:
            self.newEIDInput.setFocus()
        elif col == 1:
            self.newLastNameInput.setFocus()
        elif col == 2:
            self.newFirstNameInput.setFocus()
        elif col == 3:
            self.newBarcodeInput.setFocus()
        else:
            self.newEmailInput.setFocus()

    def fill_in_professor(self, last, first, email, col):
        self.ogEIDInput.hide()
        self.ogEIDLabel.hide()
        self.newEIDInput.hide()
        self.newEIDLabel.hide()
        self.ogBarcodeInput.hide()
        self.ogBarcodeLabel.hide()
        self.newBarcodeInput.hide()
        self.newBarcodeLabel.hide()

        self.setWindowTitle("Edit Professor")

        self.ogLastNameInput.setText(last)
        self.newLastNameInput.setText(last)
        self.ogFirstNameInput.setText(first)
        self.newFirstNameInput.setText(first)
        self.ogEmailInput.setText(email)
        self.newEmailInput.setText(email)

        if col == 0:
            self.newLastNameInput.setFocus()
        elif col == 1:
            self.newFirstNameInput.setFocus()
        else:
            self.newEmailInput.setFocus()

    def ok_button_clicked(self):
        if self.windowTitle() == "Edit Student":
            student = {"eid": self.newEIDInput.text(), "barcode": self.newBarcodeInput.text(),
                       "last_name": self.newLastNameInput.text(), "first_name": self.newFirstNameInput.text(),
                       "email": self.newEmailInput.text()}
            result = Database.update_student(self.ogEIDInput.text(), student)
            if result is True:
                self.accept()
            else:
                print("couldn't update student")
        else:
            og_prof = {"last_name": self.ogLastNameInput.text(), "first_name": self.ogFirstNameInput.text(),
                       "email": self.ogEmailInput.text()}
            professor = {"last_name": self.newLastNameInput.text(), "first_name": self.newFirstNameInput.text(),
                         "email": self.newEmailInput.text()}
            result = Database.update_professor(og_prof, professor)
            if result is True:
                self.accept()
            else:
                print("couldn't update professor")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = EditDialog()
    window.show()
    app.exec()
