import sys
from PyQt5 import QtWidgets

from gui.SignInOrOutPopup import Ui_Form


class SignInPopup(QtWidgets, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super(SignInPopup, self).__init__(*args, **kwargs)
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = SignInPopup()
    window.show()
    app.exec()
