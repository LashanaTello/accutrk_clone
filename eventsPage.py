# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eventsPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UpcomingEvents(object):
    def setupUi(self, UpcomingEvents):
        UpcomingEvents.setObjectName("UpcomingEvents")
        UpcomingEvents.resize(720, 538)
        self.closeButton = QtWidgets.QPushButton(UpcomingEvents)
        self.closeButton.setGeometry(QtCore.QRect(600, 490, 99, 27))
        self.closeButton.setObjectName("closeButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(UpcomingEvents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 691, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(29)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.eventsCalendar = QtWidgets.QCalendarWidget(self.verticalLayoutWidget)
        self.eventsCalendar.setMinimumSize(QtCore.QSize(550, 0))
        self.eventsCalendar.setObjectName("eventsCalendar")
        self.verticalLayout_2.addWidget(self.eventsCalendar, 0, QtCore.Qt.AlignHCenter)
        self.eventsList = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.eventsList.setObjectName("eventsList")
        self.eventsList.setColumnCount(3)
        self.eventsList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.eventsList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.eventsList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.eventsList.setHorizontalHeaderItem(2, item)
        self.eventsList.horizontalHeader().setDefaultSectionSize(229)
        self.eventsList.horizontalHeader().setSortIndicatorShown(True)
        self.verticalLayout_2.addWidget(self.eventsList)

        self.retranslateUi(UpcomingEvents)
        QtCore.QMetaObject.connectSlotsByName(UpcomingEvents)

    def retranslateUi(self, UpcomingEvents):
        _translate = QtCore.QCoreApplication.translate
        UpcomingEvents.setWindowTitle(_translate("UpcomingEvents", "Events Calendar"))
        self.closeButton.setText(_translate("UpcomingEvents", "Close"))
        item = self.eventsList.horizontalHeaderItem(0)
        item.setText(_translate("UpcomingEvents", "Title"))
        item = self.eventsList.horizontalHeaderItem(1)
        item.setText(_translate("UpcomingEvents", "Date"))
        item = self.eventsList.horizontalHeaderItem(2)
        item.setText(_translate("UpcomingEvents", "Time"))