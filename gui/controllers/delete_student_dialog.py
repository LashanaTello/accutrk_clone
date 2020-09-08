import sys
from PyQt5 import QtWidgets

from gui.DeleteStudentDialog import Ui_DeleteStudentDialog
from server import Database


class DeleteStudentDialog(QtWidgets.QDialog, Ui_DeleteStudentDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(DeleteStudentDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.eid = ""
        self.first = ""
        self.last = ""
        self.email = ""

        self.init_ui()

    def init_ui(self):
        self.cancelButton.clicked.connect(self.cancel_button_clicked)
        self.deleteButton.clicked.connect(self.delete_button_clicked)

    def cancel_button_clicked(self):
        self.reject()

    def delete_button_clicked(self):
        if self.windowTitle() == "Delete Student":
            result = Database.remove_student(self.eid)
            if result is True:
                self.accept()
            else:
                print("could not delete student")
        else:
            result = Database.remove_professor(self.first, self.last, self.email)
            if result is True:
                self.accept()
            else:
                print("could not delete professor")

    def fill_in(self, first, last, eid):
        self.nameLabel.setText(first + " " + last)
        self.eid = eid

    def fill_in_prof(self, first, last, email):
        self.nameLabel.setText(first + " " + last)
        self.first = first
        self.last = last
        self.email = email
        self.setWindowTitle("Delete Professor?")
        self.message.setText("Are you sure you want to delete this professor?")
        self.deleteButton.setText("Delete Professor")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = DeleteStudentDialog()
    window.show()
    app.exec()
