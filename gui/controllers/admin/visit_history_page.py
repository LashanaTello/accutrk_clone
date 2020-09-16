import sys
from PyQt5 import QtWidgets

from gui.VisitHistoryPage import Ui_VisitHistoryPage


class VisitHistoryPage(QtWidgets.QDialog, Ui_VisitHistoryPage):
    def __init__(self, *args, obj=None, **kwargs):
        super(VisitHistoryPage, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.init_ui()

    def init_ui(self):
        self.editButton.hide()
        self.closeButton.clicked.connect(self.close_button_clicked)

    def close_button_clicked(self):
        self.close()

    def adjust_for_edit(self):
        self.setWindowTitle("Edit Visit History")
        self.editButton.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = VisitHistoryPage()
    window.show()
    app.exec()
