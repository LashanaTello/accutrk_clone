import sys
from PyQt5 import QtWidgets

from gui.MediaListPopup import Ui_MediaListPopup


class MediaListPopup(QtWidgets.QDialog, Ui_MediaListPopup):
    def __init__(self, *args, obj=None, **kwargs):
        super(MediaListPopup, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.closeButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MediaListPopup()
    window.show()
    app.exec()
