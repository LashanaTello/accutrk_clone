import sys
from PyQt5 import QtWidgets

from gui.EditDialog import Ui_EditDialog


class EditDialog(QtWidgets.QDialog, Ui_EditDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(EditDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.init_ui()

    def init_ui(self):
        self.cancelButton.clicked.connect(self.cancel_button_clicked)

    def cancel_button_clicked(self):
        self.close()

    def fill_in(self, eid, last, first, barcode, email, col):
        self.ogEIDInput.setText(eid)
        self.newEIDInput.setText(eid)
        self.ogBarcodeInput.setText(barcode)
        self.newBarcodeInput.setText(barcode)
        self.ogLastNameInput.setText(last)
        self.newLastNameInput.setText(last)
        self.ogFirstNameInput.setText(first)
        self.newFirstNameInput.setText(first)
        self.ogEmailInput.setText(email)
        self.newEmailInput.setText(email)

        if col == 0:
            self.newEIDInput.setFocus()
        elif col == 1:
            self.newLastNameInput.setFocus()
        elif col == 2:
            self.newFirstNameInput.setFocus()
        elif col == 3:
            self.newBarcodeInput.setFocus()
        else:
            self.newEmailInput.setFocus()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = EditDialog()
    window.show()
    app.exec()
