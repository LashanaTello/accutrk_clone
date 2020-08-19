import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from gui.RegisterPopup import Ui_Register


class RegisterPopup(QtWidgets.QDialog, Ui_Register):
    def __init__(self, *args, obj=None, **kwargs):
        super(RegisterPopup, self).__init__(*args, **kwargs)
        self.setupUi(self)

        rx = QtCore.QRegExp("[0-9]{8}")
        validator = QtGui.QRegExpValidator(rx)
        self.IDInput.setValidator(validator)
        self.IDInput.setFocus()

        rx = QtCore.QRegExp("[0-9]{14}")
        validator = QtGui.QRegExpValidator(rx)
        self.barcodeInput.setValidator(validator)

        rx = QtCore.QRegExp("[-a-zA-Z]{25}")
        validator = QtGui.QRegExpValidator(rx)
        self.lastnameInput.setValidator(validator)
        self.firstnameInput.setValidator(validator)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = RegisterPopup()
    window.show()
    app.exec()
