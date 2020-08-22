import sys
from PyQt5 import QtWidgets

from gui.MediaListPopup import Ui_MediaListPopup
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MediaListPopup()
    window.show()
    app.exec()
