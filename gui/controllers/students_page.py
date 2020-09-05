import sys
from PyQt5 import QtWidgets

from gui.StudentsPage import Ui_StudentsPage


class StudentsPage(QtWidgets.QDialog, Ui_StudentsPage):
    def __init__(self, *args, obj=None, **kwargs):
        super(StudentsPage, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.init_ui()

    def init_ui(self):
        self.closeButton.clicked.connect(self.close_button_clicked)
        self.searchByComboBox.setPlaceholderText("Search by...")

    def close_button_clicked(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = StudentsPage()
    window.show()
    app.exec()
