import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from gui.RegisterPopup import Ui_Register
from gui.controllers.message_popup import MessagePopup
from gui.helperfunctions.helpers import combine_into_class
from server import Database


class RegisterPopup(QtWidgets.QDialog, Ui_Register):
    def __init__(self, *args, obj=None, **kwargs):
        super(RegisterPopup, self).__init__(*args, **kwargs)
        self.setupUi(self)

        rx = QtCore.QRegExp("[0-9]{8}")
        validator = QtGui.QRegExpValidator(rx)
        self.IDInput.setValidator(validator)

        rx = QtCore.QRegExp("[0-9]{14}")
        validator = QtGui.QRegExpValidator(rx)
        self.barcodeInput.setValidator(validator)

        rx = QtCore.QRegExp("[-a-zA-Z ]{25}")
        validator = QtGui.QRegExpValidator(rx)
        self.lastnameInput.setValidator(validator)
        self.firstnameInput.setValidator(validator)

        rx = QtCore.QRegExp("^[a-z0-9+_.-]+@[a-z0-9.-]+$")
        validator = QtGui.QRegExpValidator(rx)
        self.emailInput.setValidator(validator)

        rx = QtCore.QRegExp("[-a-zA-Z0-9 ]+")
        validator = QtGui.QRegExpValidator(rx)
        self.classListComboBox.setValidator(validator)

        self.classes = []
        self.class_set = set()

        self.popup = None

        self.init_ui()

    def init_ui(self):
        class_list = Database.get_all_class_names()
        formatted_class_list = []
        for a_class in class_list:
            formatted_class_list.append(combine_into_class(a_class["subject"], a_class["catalog"], a_class["section"]))
            self.classes.append(a_class)
        self.classListComboBox.addItems(formatted_class_list)

        completer = QtWidgets.QCompleter(formatted_class_list)
        completer.setFilterMode(QtCore.Qt.MatchContains)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.classListComboBox.setCompleter(completer)

        self.classListComboBox.setCurrentIndex(-1)

        self.classListComboBox.currentIndexChanged.connect(self.add_class_to_table)
        self.classTable.itemDoubleClicked.connect(self.table_item_double_clicked)

    def table_item_double_clicked(self):
        selected_class = self.classTable.selectedItems()
        tup = (selected_class[0].text(), selected_class[1].text(), selected_class[2].text())
        self.class_set.remove(tup)
        self.classTable.removeRow(self.classTable.currentRow())

    def add_class_to_table(self):
        if self.classListComboBox.currentIndex() < 0 or self.classListComboBox.currentIndex() >= len(self.classes):
            return

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

        # need to create custom sort
        self.classTable.sortItems(0, QtCore.Qt.AscendingOrder)

    def take_id(self, student_num):
        if len(student_num) == 8:
            self.IDInput.setText(student_num)
            self.barcodeInput.setFocus()
        else:
            self.barcodeInput.setText(student_num)
            self.IDInput.setFocus()

    def accept(self) -> None:
        self.popup = MessagePopup()
        if self.IDInput.text() == "" or (self.IDInput.text() == "" and self.barcodeInput.text() == ""):
            message = "Enter valid ID (8 digits) or barcode (14 digits)"
            self.popup.show_message(message)
            self.IDInput.setFocus()
            return

        if self.firstnameInput.text() == "" or self.lastnameInput.text() == "":
            message = "Enter first name and last name"
            self.popup.show_message(message)
            self.firstnameInput.setFocus()
            return

        if self.classTable.rowCount() == 0:
            message = "Select a class"
            self.popup.show_message(message)
            self.classListComboBox.setFocus()
            return

        success = Database.add_student(self.IDInput.text(), self.firstnameInput.text(), self.lastnameInput.text(),
                                       self.barcodeInput.text(), self.emailInput.text())
        message = ""
        if success:
            count = 0
            while count < self.classTable.rowCount():
                self.classTable.selectRow(count)
                selected_class = self.classTable.selectedItems()
                result = Database.register_student(self.IDInput.text(), self.firstnameInput.text(),
                                                   self.lastnameInput.text(), selected_class[0].text(),
                                                   selected_class[1].text(), selected_class[2].text())
                a_class = combine_into_class(selected_class[0].text(), selected_class[1].text(),
                                             selected_class[2].text())
                if type(result) is tuple and result == (True, True):
                    message += "Student was successfully registered for " + a_class + "\n"
                    count += 1
                elif type(result) is tuple and result == (True, False):
                    message += "Student is already registered for " + a_class + "\n"
                elif type(result) is not tuple and result == False:
                    message += "The class " + a_class + " does not exist\n"
        else:
            message = "Student could not be added to system because student is already in the system"

        print(message)
        self.popup.show_message(message)
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = RegisterPopup()
    window.show()
    app.exec()
