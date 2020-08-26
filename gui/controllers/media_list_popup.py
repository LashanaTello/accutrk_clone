import sys
from PyQt5 import QtWidgets

from gui.MediaListPopup import Ui_MediaListPopup
from gui.helperfunctions.helpers import convert_time
from server import MediaDatabase


class MediaListPopup(QtWidgets.QDialog, Ui_MediaListPopup):
    def __init__(self, *args, obj=None, **kwargs):
        super(MediaListPopup, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.closeButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.close()

    def show_all_media(self):
        all_media = MediaDatabase.get_all_media()
        for media in all_media:
            self.mediaTable.setRowCount(self.mediaTable.rowCount() + 1)
            row = self.mediaTable.rowCount() - 1
            self.mediaTable.setItem(row, 0, QtWidgets.QTableWidgetItem(media["media_barcode"]))
            self.mediaTable.setItem(row, 1, QtWidgets.QTableWidgetItem(media["media_title"]))
            self.mediaTable.setItem(row, 2, QtWidgets.QTableWidgetItem(media["media_type"]))
        self.mediaTable.sortItems(1, 0)

    def show_available_media(self):
        self.setWindowTitle("Available Media")

    def show_out_media(self):
        self.setWindowTitle("Media Out")
        self.mediaTable.setColumnCount(6)
        self.mediaTable.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Time Out"))
        self.mediaTable.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem("Last Name"))
        self.mediaTable.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem("First Name"))
        self.mediaTable.horizontalHeader().setDefaultSectionSize(180)

        data = MediaDatabase.get_checkout_list()
        for entry in data:
            self.mediaTable.setRowCount(self.mediaTable.rowCount() + 1)
            row = self.mediaTable.rowCount() - 1
            self.mediaTable.setItem(row, 0, QtWidgets.QTableWidgetItem(entry["media_barcode"]))
            self.mediaTable.setItem(row, 1, QtWidgets.QTableWidgetItem(entry["media_title"]))
            self.mediaTable.setItem(row, 2, QtWidgets.QTableWidgetItem(entry["media_type"]))
            self.mediaTable.setItem(row, 3, QtWidgets.QTableWidgetItem(convert_time(entry["check_out_time"])))
            self.mediaTable.setItem(row, 4, QtWidgets.QTableWidgetItem(entry["last_name"]))
            self.mediaTable.setItem(row, 5, QtWidgets.QTableWidgetItem(entry["first_name"]))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MediaListPopup()
    window.show()
    app.exec()
