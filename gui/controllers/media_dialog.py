import sys
from PyQt5 import QtWidgets, QtGui

from gui.MediaCheckoutDialog import Ui_MediaDialog
from gui.controllers.media_checkout import MediaCheckoutPage


class MediaCheckoutDialog(QtWidgets.QDialog, Ui_MediaDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(MediaCheckoutDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # self.studentIDInput.setMaxLength(14)
        # validator = QtGui.QIntValidator()
        # self.studentIDInput.setValidator(validator)

        self.media_checkout_page = None

        self.init_ui()

    def init_ui(self):
        self.studentIDInput.textChanged.connect(self.handle_input_changed)

    def handle_input_changed(self, text):
        print("contents changed to:", text)

    def accept(self) -> None:
        self.media_checkout_page = MediaCheckoutPage()
        self.media_checkout_page.show()
        self.hide()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MediaCheckoutDialog()
    window.show()
    app.exec()
