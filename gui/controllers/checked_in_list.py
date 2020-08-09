import sys
from PyQt5 import QtWidgets

from gui.CheckedInListPage import Ui_MainWindow


class CheckedInListPage(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(CheckedInListPage, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.init_ui()

    def init_ui(self):
        self.closeWindowButton.clicked.connect(self.close_button_clicked)

    def close_button_clicked(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = CheckedInListPage()
    window.show()
    app.exec()
