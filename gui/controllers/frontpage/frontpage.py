import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from gui.FrontPage import Ui_MainWindow
from gui.controllers.frontpage.checked_in_list import CheckedInListPage
from gui.controllers.frontpage.events_dialog import EventsDialog
from gui.controllers.frontpage.media_dialog import MediaCheckoutDialog
from gui.controllers.frontpage.sign_in_dialog import SignInDialog
from gui.controllers.message_popup import MessagePopup
from gui.controllers.frontpage.register_popup import RegisterPopup
from gui.controllers.admin.admin_page import AdminPage

from server import Database


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.userInput.hide()

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
        self.popup = None
        self.register_popup = None
        self.admin_page = None

        self.init_ui()

    def init_ui(self):
        self.whosInButton.clicked.connect(self.whos_in_clicked)
        self.eventsButton.clicked.connect(self.events_button_clicked)
        self.mediaButton.clicked.connect(self.media_button_clicked)
        self.evalUserInputLine.textChanged.connect(self.handle_input_line_change)
        self.evalUserInputLine.returnPressed.connect(self.handle_input_submit)
        self.userInput.returnPressed.connect(self.handle_password_submit)

    def whos_in_clicked(self):
        self.logged_in = CheckedInListPage()
        self.logged_in.show()

    def events_button_clicked(self):
        self.event_dialog = EventsDialog()
        self.event_dialog.show()

    def media_button_clicked(self):
        self.media_dialog = MediaCheckoutDialog()
        self.media_dialog.show()

    def handle_input_line_change(self, text):
        print(self.evalUserInputLine.hasAcceptableInput())

    def handle_input_submit(self):
        if self.evalUserInputLine.text().isalpha():
            self.evalUserInputLine.setReadOnly(True)
            self.userInput.show()
            self.userInput.setFocus()
        elif self.evalUserInputLine.text().isdigit():
            result = self.evaluate_input(self.evalUserInputLine.text())

            if type(result) is tuple and result[0] == True:
                self.popup = MessagePopup()
                self.popup.fill_in(result[1] + " " + result[2], "SIGN OUT SUCCESS")
                self.popup.show()
                QtCore.QTimer.singleShot(5000, self.popup.close)
                self.evalUserInputLine.setText("")
            elif type(result) is tuple and result[0] == False:
                self.popup = MessagePopup()
                self.popup.fill_in(result[1] + " " + result[2], "SIGN OUT FAILURE")
                self.popup.show()
                QtCore.QTimer.singleShot(6000, self.popup.close)
            elif result is None:
                self.register_popup = RegisterPopup()
                self.register_popup.take_id(self.evalUserInputLine.text())
                self.register_popup.show()
            else:
                self.signin_dialog = SignInDialog()
                self.signin_dialog.fill_in(result)
                self.signin_dialog.show()
                self.evalUserInputLine.setText("")

    def update_time(self):
        self.currentTime.setDateTime(QtCore.QDateTime.currentDateTime())

    def evaluate_input(self, student_id):
        return Database.evaluate_input(student_id)

    def handle_password_submit(self):
        self.admin_page = AdminPage()
        self.admin_page.show()
        self.hide()
        self.admin_page.finished.connect(self.reopen)
        self.userInput.hide()
        self.evalUserInputLine.clear()
        self.evalUserInputLine.setReadOnly(False)
        self.evalUserInputLine.setFocus()

    def reopen(self):
        self.show()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
