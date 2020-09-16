import sys
from PyQt5 import QtWidgets

from gui.ManualSignOutPage import Ui_ManualSignOutPage


class SignOutPage(QtWidgets.QDialog, Ui_ManualSignOutPage):
    def __init__(self, *args, obj=None, **kwargs):
        super(SignOutPage, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.init_ui()

    def init_ui(self):
        self.closeButton.clicked.connect(self.close_button_clicked)

    def close_button_clicked(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = SignOutPage()
    window.show()
    app.exec()
