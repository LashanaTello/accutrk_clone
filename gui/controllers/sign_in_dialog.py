import sys
from PyQt5 import QtWidgets

from gui.SignInDialog import Ui_SignInDialog


class SignInDialog(QtWidgets.QDialog, Ui_SignInDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(SignInDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.init_ui()

    def init_ui(self):
        self.cancelButton.clicked.connect(self.cancel_button_clicked)

    def cancel_button_clicked(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = SignInDialog()
    window.show()
    app.exec()
