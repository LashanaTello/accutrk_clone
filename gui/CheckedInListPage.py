# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkedInListPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 878)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginList = QtWidgets.QTableWidget(self.centralwidget)
        self.loginList.setGeometry(QtCore.QRect(0, 70, 1121, 621))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(99)
        sizePolicy.setVerticalStretch(99)
        sizePolicy.setHeightForWidth(self.loginList.sizePolicy().hasHeightForWidth())
        self.loginList.setSizePolicy(sizePolicy)
        self.loginList.setMinimumSize(QtCore.QSize(1041, 621))
        self.loginList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.loginList.setShowGrid(True)
        self.loginList.setGridStyle(QtCore.Qt.SolidLine)
        self.loginList.setRowCount(0)
        self.loginList.setObjectName("loginList")
        self.loginList.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.loginList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.loginList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.loginList.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.loginList.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.loginList.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.loginList.setHorizontalHeaderItem(5, item)
        self.loginList.horizontalHeader().setCascadingSectionResizes(False)
        self.loginList.horizontalHeader().setDefaultSectionSize(186)
        self.loginList.horizontalHeader().setSortIndicatorShown(False)
        self.closeWindowButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeWindowButton.setGeometry(QtCore.QRect(1020, 10, 99, 27))
        self.closeWindowButton.setObjectName("closeWindowButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(450, 730, 211, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.studentsPresent = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.studentsPresent.setObjectName("studentsPresent")
        self.horizontalLayout.addWidget(self.studentsPresent)
        self.numberOfStudents = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.numberOfStudents.setTextFormat(QtCore.Qt.AutoText)
        self.numberOfStudents.setAlignment(QtCore.Qt.AlignCenter)
        self.numberOfStudents.setObjectName("numberOfStudents")
        self.horizontalLayout.addWidget(self.numberOfStudents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Who\'s Logged In"))
        item = self.loginList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Last Name"))
        item = self.loginList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "First Name"))
        item = self.loginList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Log-In Time"))
        item = self.loginList.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Log-Out Time"))
        item = self.loginList.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Class"))
        item = self.loginList.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Activity"))
        self.closeWindowButton.setText(_translate("MainWindow", "Close"))
        self.studentsPresent.setText(_translate("MainWindow", "Students Present:"))
        self.numberOfStudents.setText(_translate("MainWindow", "0"))
