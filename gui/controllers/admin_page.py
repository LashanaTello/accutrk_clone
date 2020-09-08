import sys
from PyQt5 import QtWidgets, QtCore

from gui.AdminPage import Ui_AdminPage
from gui.controllers.students_page import StudentsPage
from gui.controllers.professors_page import ProfessorsPage


class AdminPage(QtWidgets.QDialog, Ui_AdminPage):
    def __init__(self, *args, obj=None, **kwargs):
        super(AdminPage, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.students_page = None
        self.professors_page = None

        self.init_ui()

    def init_ui(self):
        self.returnToMainPageButton.clicked.connect(self.return_button_clicked)
        self.visitorsButton.clicked.connect(self.visitors_button_clicked)
        self.coursesButton.clicked.connect(self.courses_button_clicked)
        self.visitHistoryButton.clicked.connect(self.visit_history_button_clicked)
        self.mediaButton.clicked.connect(self.media_button_clicked)
        self.eventsButton.clicked.connect(self.events_button_clicked)
        self.appointmentButton.clicked.connect(self.appt_button_clicked)
        self.comButton.clicked.connect(self.com_button_clicked)
        self.semesterButton.clicked.connect(self.semester_button_clicked)
        self.databaseButton.clicked.connect(self.database_button_clicked)
        self.systemButton.clicked.connect(self.system_button_clicked)
        self.userServicesButton.clicked.connect(self.user_services_button_clicked)

        self.studentsButton.clicked.connect(self.students_button_clicked)
        self.professorButton.clicked.connect(self.professors_button_clicked)

    def return_button_clicked(self):
        self.close()

    def visitors_button_clicked(self):
        self.stackedWidget.setCurrentIndex(0)
        self.stackContainer.setTitle(self.visitorsButton.text())

    def courses_button_clicked(self):
        self.stackedWidget.setCurrentIndex(1)
        self.stackContainer.setTitle(self.coursesButton.text())

    def visit_history_button_clicked(self):
        self.stackedWidget.setCurrentIndex(2)
        self.stackContainer.setTitle(self.visitHistoryButton.text())

    def media_button_clicked(self):
        self.stackedWidget.setCurrentIndex(3)
        self.stackContainer.setTitle(self.mediaButton.text())

    def events_button_clicked(self):
        self.stackedWidget.setCurrentIndex(4)
        self.stackContainer.setTitle(self.eventsButton.text())

    def appt_button_clicked(self):
        self.stackedWidget.setCurrentIndex(5)
        self.stackContainer.setTitle(self.appointmentButton.text())

    def com_button_clicked(self):
        self.stackedWidget.setCurrentIndex(6)
        self.stackContainer.setTitle(self.comButton.text())

    def semester_button_clicked(self):
        self.stackedWidget.setCurrentIndex(7)
        self.stackContainer.setTitle(self.semesterButton.text())

    def database_button_clicked(self):
        self.stackedWidget.setCurrentIndex(8)
        self.stackContainer.setTitle(self.databaseButton.text())

    def system_button_clicked(self):
        self.stackedWidget.setCurrentIndex(9)
        self.stackContainer.setTitle(self.systemButton.text())

    def user_services_button_clicked(self):
        self.stackedWidget.setCurrentIndex(10)
        self.stackContainer.setTitle(self.userServicesButton.text())

    def students_button_clicked(self):
        self.students_page = StudentsPage()
        self.students_page.open()
        self.hide()
        self.students_page.finished.connect(self.reopen)

    def professors_button_clicked(self):
        self.professors_page = ProfessorsPage()
        self.professors_page.open()
        self.hide()
        self.professors_page.finished.connect(self.reopen)

    def reopen(self):
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = AdminPage()
    window.show()
    app.exec()
