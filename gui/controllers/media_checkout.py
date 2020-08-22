import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from gui.MediaCheckoutPage import Ui_MainWindow
from gui.controllers.media_list_popup import MediaListPopup


class MediaCheckoutPage(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MediaCheckoutPage, self).__init__(*args, **kwargs)
        self.setupUi(self)

        rx = QtCore.QRegExp("[0-9]+")
        validator = QtGui.QRegExpValidator(rx)
        self.mediaIDInput.setValidator(validator)
        self.mediaIDInput.setFocus()

        self.media_popup = None

        self.init_ui()

    def init_ui(self):
        self.closeButton.clicked.connect(self.close_button_clicked)
        self.outMediaButton.clicked.connect(self.out_button_clicked)
        self.availableMediaButton.clicked.connect(self.available_button_clicked)
        self.allMediaButton.clicked.connect(self.all_button_clicked)

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

    def fill_in(self, eid, barcode, first, last):
        self.studentIDInput.setText(eid)
        self.studentBarcodeInput.setText(barcode)
        self.studentFirstNameInput.setText(first)
        self.studentLastNameInput.setText(last)
        self.tableLabel.setText(first + " " + last + " has:")
        self.mediaIDInput.setFocus()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MediaCheckoutPage()
    window.show()
    app.exec()
