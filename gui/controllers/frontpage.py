import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from gui.FrontPage import Ui_MainWindow
from gui.controllers.checked_in_list import CheckedInListPage
from gui.controllers.events import EventDialog
from gui.controllers.media_dialog import MediaCheckoutDialog
from gui.controllers.sign_in_dialog import SignInDialog

from server import Database


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.update_time()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        rx = QtCore.QRegExp("[a-zA-Z0-9]{8}|[a-zA-Z0-9]{14}")
        validator = QtGui.QRegExpValidator(rx)
        self.evalUserInputLine.setValidator(validator)
        self.evalUserInputLine.setFocus()

        self.logged_in = None
        self.event_dialog = None
        self.media_page = None
        self.media_dialog = None
        self.signin_dialog = None

        self.init_ui()

    def init_ui(self):
        self.whosInButton.clicked.connect(self.whos_in_clicked)
        self.eventsButton.clicked.connect(self.events_button_clicked)
        self.mediaButton.clicked.connect(self.media_button_clicked)
        self.evalUserInputLine.textChanged.connect(self.handle_input_line_change)
        self.evalUserInputLine.returnPressed.connect(self.handle_input_submit)

    def whos_in_clicked(self):
        self.logged_in = CheckedInListPage()
        self.logged_in.show()

    def events_button_clicked(self):
        self.event_dialog = EventDialog()
        self.event_dialog.show()

    def media_button_clicked(self):
        self.media_dialog = MediaCheckoutDialog()
        self.media_dialog.show()

    def handle_input_line_change(self, text):
        print("contents changed to:", text)
        print(self.evalUserInputLine.hasAcceptableInput())

    def handle_input_submit(self):
        print(self.evalUserInputLine.text())
        result = self.evaluate_input(self.evalUserInputLine.text())

        if result == True:
            print("signed out")
        elif result == False:
            print("couldn't sign out")
        elif result is None:
            print("nonexistent")
        else:
            self.signin_dialog = SignInDialog()
            self.signin_dialog.fill_in(result)
            self.signin_dialog.show()

    def update_time(self):
        self.currentTime.setDateTime(QtCore.QDateTime.currentDateTime())

    def evaluate_input(self, student_id):
        return Database.evaluate_input(student_id)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
