import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from gui.MediaCheckoutPage import Ui_MainWindow
from gui.controllers.media_list_popup import MediaListPopup
from gui.controllers.message_popup import MessagePopup
from gui.helperfunctions.helpers import convert_time
from server import MediaDatabase


class MediaCheckoutPage(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MediaCheckoutPage, self).__init__(*args, **kwargs)
        self.setupUi(self)

        rx = QtCore.QRegExp("[0-9]+")
        validator = QtGui.QRegExpValidator(rx)
        self.mediaIDInput.setValidator(validator)
        self.mediaIDInput.setFocus()

        self.eid = ""
        self.barcode = ""
        self.first_name = ""
        self.last_name = ""
        self.media_popup = None
        self.popup = None

        self.init_ui()

    def init_ui(self):
        self.closeButton.clicked.connect(self.close_button_clicked)
        self.outMediaButton.clicked.connect(self.out_button_clicked)
        self.availableMediaButton.clicked.connect(self.available_button_clicked)
        self.allMediaButton.clicked.connect(self.all_button_clicked)
        self.processButton.clicked.connect(self.process_button_clicked)

    def close_button_clicked(self):
        self.close()

    def out_button_clicked(self):
        self.media_popup = MediaListPopup()
        self.media_popup.show_out_media()
        self.media_popup.show()

    def available_button_clicked(self):
        self.media_popup = MediaListPopup()
        self.media_popup.show_available_media()
        self.media_popup.show()

    def all_button_clicked(self):
        self.media_popup = MediaListPopup()
        self.media_popup.show_all_media()
        self.media_popup.show()

    def enter_data(self, eid, barcode, first, last, checkouts):
        self.fill_in(eid, barcode, first, last, checkouts)
        self.eid = eid
        self.barcode = barcode
        self.first_name = first
        self.last_name = last
        self.mediaIDInput.setFocus()

    def fill_in(self, eid, barcode, first, last, checkouts=[]):
        self.studentIDInput.setText(eid)
        self.studentBarcodeInput.setText(barcode)
        self.studentFirstNameInput.setText(first)
        self.studentLastNameInput.setText(last)
        self.tableLabel.setText(first + " " + last + " has:")
        for entry in checkouts:
            self.borrowTable.setRowCount(self.borrowTable.rowCount() + 1)
            row = self.borrowTable.rowCount() - 1
            self.borrowTable.setItem(row, 0, QtWidgets.QTableWidgetItem(entry["media_barcode"]))
            self.borrowTable.setItem(row, 1, QtWidgets.QTableWidgetItem(entry["media_title"]))
            self.borrowTable.setItem(row, 2, QtWidgets.QTableWidgetItem(entry["media_type"]))
            self.borrowTable.setItem(row, 3, QtWidgets.QTableWidgetItem(convert_time(entry["check_out_time"])))

    def clear_all(self):
        self.mediaIDInput.clear()
        self.mediaTypeInput.clear()
        self.mediaTitleInput.clear()
        self.studentIDInput.clear()
        self.studentBarcodeInput.clear()
        self.studentLastNameInput.clear()
        self.studentFirstNameInput.clear()
        self.borrowTable.clearContents()
        self.borrowTable.setRowCount(0)
        self.tableLabel.setText("Student has:")
        self.processButton.setText("Process")

    def process_button_clicked(self):
        message = ""
        error = False
        if self.processButton.text() == "Process":
            result = MediaDatabase.evaluate_media_input(self.mediaIDInput.text())
            if type(result) is tuple and result[0] == "out":
                self.mediaTypeInput.setText(result[1]["media_type"])
                self.mediaTitleInput.setText(result[1]["media_title"])
                if self.studentIDInput.text() == "":
                    self.fill_in(self.eid, self.barcode, self.first_name, self.last_name,
                                 MediaDatabase.get_student_checkouts(self.eid))
                self.processButton.setText("Check OUT")
            elif type(result) is tuple and result[0] == "in":
                self.mediaTypeInput.setText(result[1]["media_type"])
                self.mediaTitleInput.setText(result[1]["media_title"])
                if self.borrowTable.rowCount() > 0:
                    self.fill_in(result[1]["eid"], result[1]["barcode"], result[1]["first_name"],
                                 result[1]["last_name"])
                else:
                    self.fill_in(result[1]["eid"], result[1]["barcode"], result[1]["first_name"],
                                 result[1]["last_name"], result[2])

                self.processButton.setText("Check IN")
            else:
                message = "Media does not exist"
                error = True
        elif self.processButton.text() == "Check OUT":
            media = {"media_barcode": self.mediaIDInput.text(), "media_title": self.mediaTitleInput.text(),
                     "media_type": self.mediaTypeInput.text()}
            student_info = {"eid": self.studentIDInput.text(), "barcode": self.studentBarcodeInput.text(),
                            "first_name": self.studentFirstNameInput.text(),
                            "last_name": self.studentLastNameInput.text()}
            result = MediaDatabase.check_out(media, student_info)
            self.clear_all()
            if result == False:
                message = "Failed to check out materials under student\n"
                message += ("NAME: " + self.studentFirstNameInput.text() + " " + self.studentLastNameInput.text() + "\n")
                message += "STUDENT ID: " + self.studentIDInput.text()
                message += "MEDIA ID: " + self.mediaIDInput.text()
                error = True
        else:
            result = MediaDatabase.check_in(self.mediaIDInput.text())
            self.clear_all()
            if result == False:
                message = "Failed to check in materials\n"
                message += ("NAME: " + self.studentFirstNameInput.text() + " " + self.studentLastNameInput.text() + "\n")
                message += "STUDENT ID: " + self.studentIDInput.text()
                message += "MEDIA ID: " + self.mediaIDInput.text()
                error = True

        if error is True:
            self.popup = MessagePopup()
            self.popup.show_message(message)
        self.mediaIDInput.setFocus()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MediaCheckoutPage()
    window.show()
    app.exec()
