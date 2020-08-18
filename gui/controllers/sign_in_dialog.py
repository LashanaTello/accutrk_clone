import sys
from PyQt5 import QtWidgets, QtCore
import pytz
import datetime

from gui.SignInDialog import Ui_SignInDialog
from gui.controllers.sign_in_popup import SignInPopup

from server import Database


class SignInDialog(QtWidgets.QDialog, Ui_SignInDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(SignInDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.student_name = {"first": "", "last": ""}
        self.popup = None

        self.init_ui()

    def init_ui(self):
        self.cancelButton.clicked.connect(self.cancel_button_clicked)
        self.eventList.itemDoubleClicked.connect(self.event_item_double_clicked)
        self.signInButton.clicked.connect(self.sign_in_button_clicked)

    def cancel_button_clicked(self):
        self.close()

    def event_item_double_clicked(self):
        self.eventList.setCurrentRow(-1)

    def sign_in_button_clicked(self):
        login_time = datetime.datetime.utcnow()
        logout_time = ""
        selected_class = self.classTable.selectedItems()

        student = {"eid": self.studentEIDLabel.text(), "barcode": self.studentBarcodeLabel.text(),
                   "first_name": self.student_name["first"], "last_name": self.student_name["last"],
                   "subject": selected_class[0].text(), "catalog": selected_class[1].text(),
                   "section": selected_class[2].text(), "login_time": login_time, "logout_time": logout_time,
                   "service": self.activityList.currentItem().text()
                   }

        if Database.signn_in(student):
            self.popup = SignInPopup()
            self.popup.fill_in(self.studentNameLabel.text(), "SIGN IN SUCCESS")
            self.popup.show()
            self.close()
            QtCore.QTimer.singleShot(5000, self.popup.close)
        else:
            print("Failed to sign in student")

    def fill_in(self, student):
        # some students have more than one name as a first name so store their name from the db to ensure it's correct
        # for later use
        self.student_name["first"] = student["first_name"]
        self.student_name["last"] = student["last_name"]

        self.studentEIDLabel.setText(student["eid"])
        self.studentBarcodeLabel.setText(student["barcode"])
        self.studentNameLabel.setText(student["first_name"] + " " + student["last_name"])
        self.semesterList.addItem(Database.get_semester_name())
        self.semesterList.setCurrentRow(0)

        activities = Database.get_all_activities()
        for activity in activities:
            self.activityList.addItem(activity["activity"])
        self.activityList.sortItems(0)
        self.activityList.setCurrentRow(0)

        self.classTable.setRowCount(len(student["enrolled_list"]))
        count = 0
        while count < len(student["enrolled_list"]):
            self.classTable.setItem(count, 0, QtWidgets.QTableWidgetItem(student["enrolled_list"][count]["subject"]))
            self.classTable.setItem(count, 1, QtWidgets.QTableWidgetItem(student["enrolled_list"][count]["catalog"]))
            self.classTable.setItem(count, 2, QtWidgets.QTableWidgetItem(student["enrolled_list"][count]["section"]))
            count += 1
        self.classTable.sortItems(0)
        self.classTable.selectRow(0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = SignInDialog()
    window.show()
    app.exec()
