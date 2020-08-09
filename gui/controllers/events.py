import sys
from PyQt5 import QtWidgets

from gui.EventsPage import Ui_UpcomingEvents


class EventDialog(QtWidgets.QDialogButtonBox, Ui_UpcomingEvents):
    def __init__(self, *args, obj=None, **kwargs):
        super(EventDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.init_ui()

    def init_ui(self):
        self.closeButton.clicked.connect(self.close_button_clicked)

    def close_button_clicked(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = EventDialog()
    window.show()
    app.exec()
