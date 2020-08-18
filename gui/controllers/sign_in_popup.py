import sys
from PyQt5 import QtWidgets

from gui.SignInOrOutPopup import Ui_Form


class SignInPopup(QtWidgets.QDialog, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super(SignInPopup, self).__init__(*args, **kwargs)
        self.setupUi(self)

    def fill_in(self, name, message):
        self.successLabel.setText(message)
        self.studentNameLabel.setText(name)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = SignInPopup()
    window.show()
    app.exec()
