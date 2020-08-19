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

        self.classes = []
        self.class_set = set()

        self.init_ui()

    def init_ui(self):
        class_list = Database.get_all_class_names()
        formatted_class_list = []
        for a_class in class_list:
            formatted_class_list.append(combine_into_class(a_class["subject"], a_class["catalog"], a_class["section"]))
            self.classes.append(a_class)
        self.classListComboBox.addItems(formatted_class_list)

        completer = QtWidgets.QCompleter(formatted_class_list)
        self.classListComboBox.setCompleter(completer)

        self.classListComboBox.setCurrentIndex(-1)

        self.classListComboBox.activated.connect(self.add_class_to_table)
        self.classTable.itemDoubleClicked.connect(self.table_item_double_clicked)

    def table_item_double_clicked(self):
        selected_class = self.classTable.selectedItems()
        tup = (selected_class[0].text(), selected_class[1].text(), selected_class[2].text())
        self.class_set.remove(tup)
        self.classTable.removeRow(self.classTable.currentRow())

    def add_class_to_table(self):
        curr_class = self.classes[self.classListComboBox.currentIndex()]
        new_entry = (curr_class["subject"], curr_class["catalog"], curr_class["section"])
        if new_entry not in self.class_set:
            self.class_set.add(new_entry)
            self.classTable.clearContents()
            self.classTable.setRowCount(len(self.class_set))

            count = 0
            for a_class in self.class_set:
                self.classTable.setItem(count, 0, QtWidgets.QTableWidgetItem(a_class[0]))
                self.classTable.setItem(count, 1, QtWidgets.QTableWidgetItem(a_class[1]))
                self.classTable.setItem(count, 2, QtWidgets.QTableWidgetItem(a_class[2]))
                count += 1

        self.classTable.sortItems(0, QtCore.Qt.AscendingOrder)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = RegisterPopup()
    window.show()
    app.exec()
