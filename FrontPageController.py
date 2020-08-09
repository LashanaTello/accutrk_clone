import sys
from PyQt5 import QtWidgets, uic, QtCore

from FrontPage import Ui_MainWindow
from CurrentlyLoggedInPageController import MainWindow as LoggedIn
from eventsPageController import EventDialog
from mediaCheckoutPageController import MediaCheckoutPage


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.update_time()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.logged_in = None
        self.event_dialog = None
        self.media_page = None

        self.initUI()

    def initUI(self):
        self.whosInButton.clicked.connect(self.whos_in_clicked)
        self.eventsButton.clicked.connect(self.events_button_clicked)
        self.mediaButton.clicked.connect(self.media_button_clicked)

    def whos_in_clicked(self):
        self.logged_in = LoggedIn()
        self.logged_in.show()

    def events_button_clicked(self):
        self.event_dialog = EventDialog()
        self.event_dialog.show()

    def media_button_clicked(self):
        self.media_page = MediaCheckoutPage()
        self.media_page.show()

    def update_time(self):
        self.currentTime.setDateTime(QtCore.QDateTime.currentDateTime())


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
