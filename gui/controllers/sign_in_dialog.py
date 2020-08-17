import sys
from PyQt5 import QtWidgets

from gui.SignInDialog import Ui_SignInDialog

from server import Database


class SignInDialog(QtWidgets.QDialog, Ui_SignInDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(SignInDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.init_ui()

    def init_ui(self):
        self.cancelButton.clicked.connect(self.cancel_button_clicked)

    def cancel_button_clicked(self):
        self.close()

    def fill_in(self, student):
        self.semesterList.addItem(Database.get_semester_name())
        self.semesterList.setCurrentRow(0)
        self.studentIDLabel.setText(student["barcode"])
        self.studentNameLabel.setText(student["first_name"] + " " + student["last_name"])
        for a_class in student["enrolled_list"]:
            one_class = a_class["subject"] + " " + a_class["catalog"] + " - " + a_class["section"]
            self.classList.addItem(one_class)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = SignInDialog()
    window.show()
    app.exec()
