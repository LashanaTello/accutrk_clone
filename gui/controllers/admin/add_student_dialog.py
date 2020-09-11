import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from gui.AddStudentDialog import Ui_AddStudentDialog
from server import Database


class AddStudentDialog(QtWidgets.QDialog, Ui_AddStudentDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(AddStudentDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        rx = QtCore.QRegExp("[0-9]{8}")
        validator = QtGui.QRegExpValidator(rx)
        self.EIDInput.setValidator(validator)

        rx = QtCore.QRegExp("[0-9]{14}")
        validator = QtGui.QRegExpValidator(rx)
        self.barcodeInput.setValidator(validator)

        rx = QtCore.QRegExp("[-a-zA-Z ]{25}")
        validator = QtGui.QRegExpValidator(rx)
        self.lastNameInput.setValidator(validator)
        self.firstNameInput.setValidator(validator)

        rx = QtCore.QRegExp("^[a-z0-9+_.-]+@[a-z0-9.-]+$")
        validator = QtGui.QRegExpValidator(rx)
        self.emailInput.setValidator(validator)

        self.init_ui()

    def init_ui(self):
        self.cancelButton.clicked.connect(self.cancel_button_clicked)
        self.addButton.clicked.connect(self.add_button_clicked)

    def cancel_button_clicked(self):
        self.reject()

    def add_button_clicked(self):
        if self.windowTitle() == "Add Student":
            result = Database.add_student(self.EIDInput.text(), self.firstNameInput.text(), self.lastNameInput.text(),
                                          self.barcodeInput.text(), self.emailInput.text())
            if result is True:
                self.accept()
            else:
                print("could not add student")
        else:
            result = Database.add_professor(self.firstNameInput.text(), self.lastNameInput.text(),
                                            self.emailInput.text())
            if result is True:
                self.accept()
            else:
                print("could not add professor")

    def adjust_display(self):
        self.EIDInput.hide()
        self.EIDLabel.hide()
        self.barcodeInput.hide()
        self.barcodeLabel.hide()
        self.setWindowTitle("Add Professor")

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

    window = AddStudentDialog()
    window.show()
    app.exec()
