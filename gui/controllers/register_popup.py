import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from gui.RegisterPopup import Ui_Register
from gui.helperfunctions.helpers import combine_into_class
from server import Database


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

        self.init_ui()

    def init_ui(self):
        class_list = Database.get_all_classes()
        formatted_class_list = []
        for a_class in class_list:
            formatted_class_list.append(combine_into_class(a_class["subject"], a_class["catalog"], a_class["section"]))
        self.classListComboBox.addItems(formatted_class_list)

        completer = QtWidgets.QCompleter(formatted_class_list)
        self.classListComboBox.setCompleter(completer)

        self.classListComboBox.setCurrentIndex(-1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = RegisterPopup()
    window.show()
    app.exec()
