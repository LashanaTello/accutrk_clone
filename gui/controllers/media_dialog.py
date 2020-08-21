import sys
from PyQt5 import QtWidgets, QtGui, QtCore

from gui.MediaCheckoutDialog import Ui_MediaDialog
from gui.controllers.sign_in_popup import SignInPopup
from gui.controllers.media_checkout import MediaCheckoutPage
from server import Database


class MediaCheckoutDialog(QtWidgets.QDialog, Ui_MediaDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(MediaCheckoutDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        rx = QtCore.QRegExp("[0-9]{8}|[0-9]{14}")
        validator = QtGui.QRegExpValidator(rx)
        self.studentIDInput.setValidator(validator)
        self.studentIDInput.setFocus()

        self.popup = None
        self.media_checkout_page = None

        self.init_ui()

    def init_ui(self):
        self.studentIDInput.textChanged.connect(self.handle_input_changed)

    def handle_input_changed(self):
        if not self.studentIDInput.hasAcceptableInput():
            self.validInputMessage.setText("ID must be 8 or 14 characters")
        else:
            self.validInputMessage.setText("")

    def accept(self) -> None:
        if self.studentIDInput.hasAcceptableInput():
            result = Database.get_student_data(self.studentIDInput.text())
            if result is None:
                if len(self.studentIDInput.text()) == 8:
                    message = "No student with ID " + self.studentIDInput.text() + " found"
                else:
                    message = "No student with barcode " + self.studentIDInput.text() + " found"
                self.popup = SignInPopup()
                self.popup.show_message(message)
                return
            else:
                self.media_checkout_page = MediaCheckoutPage()
                self.media_checkout_page.fill_in(result["eid"], result["barcode"], result["first_name"],
                                                 result["last_name"])
                self.media_checkout_page.show()
                self.hide()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MediaCheckoutDialog()
    window.show()
    app.exec()
