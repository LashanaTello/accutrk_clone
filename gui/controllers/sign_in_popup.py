import sys
from PyQt5 import QtWidgets

from gui.SignInOrOutPopup import Ui_Form


class SignInPopup(QtWidgets.QDialog, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super(SignInPopup, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.okButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.close()

    def fill_in(self, name, message):
        self.successLabel.setText(message)
        self.studentNameLabel.setText(name)
        self.okButton.hide()

    def show_message(self, message):
        self.studentLabel.hide()
        self.studentNameLabel.hide()
        self.successLabel.setText(message)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = SignInPopup()
    window.show()
    app.exec()
