# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manualSignOutPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ManualSignOutPage(object):
    def setupUi(self, ManualSignOutPage):
        ManualSignOutPage.setObjectName("ManualSignOutPage")
        ManualSignOutPage.resize(1281, 1022)
        self.title = QtWidgets.QLabel(ManualSignOutPage)
        self.title.setGeometry(QtCore.QRect(460, 20, 321, 51))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.closeButton = QtWidgets.QPushButton(ManualSignOutPage)
        self.closeButton.setGeometry(QtCore.QRect(1120, 20, 141, 61))
        self.closeButton.setObjectName("closeButton")
        self.selectedStudentsGroupBox = QtWidgets.QGroupBox(ManualSignOutPage)
        self.selectedStudentsGroupBox.setGeometry(QtCore.QRect(680, 100, 581, 751))
        self.selectedStudentsGroupBox.setObjectName("selectedStudentsGroupBox")
        self.selectedTable = QtWidgets.QTableWidget(self.selectedStudentsGroupBox)
        self.selectedTable.setGeometry(QtCore.QRect(20, 40, 541, 691))
        self.selectedTable.setMinimumSize(QtCore.QSize(541, 691))
        self.selectedTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.selectedTable.setObjectName("selectedTable")
        self.selectedTable.setColumnCount(10)
        self.selectedTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.selectedTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.selectedTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.selectedTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.selectedTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.selectedTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.selectedTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.selectedTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.selectedTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.selectedTable.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.selectedTable.setHorizontalHeaderItem(9, item)
        self.selectedTable.verticalHeader().setDefaultSectionSize(40)
        self.selectedTable.verticalHeader().setMinimumSectionSize(40)
        self.signOutButton = QtWidgets.QPushButton(ManualSignOutPage)
        self.signOutButton.setGeometry(QtCore.QRect(570, 950, 151, 61))
        self.signOutButton.setMinimumSize(QtCore.QSize(151, 61))
        self.signOutButton.setObjectName("signOutButton")
        self.signedInStudentsGroupBox = QtWidgets.QGroupBox(ManualSignOutPage)
        self.signedInStudentsGroupBox.setGeometry(QtCore.QRect(20, 100, 581, 751))
        self.signedInStudentsGroupBox.setObjectName("signedInStudentsGroupBox")
        self.signedInTable = QtWidgets.QTableWidget(self.signedInStudentsGroupBox)
        self.signedInTable.setGeometry(QtCore.QRect(20, 40, 541, 691))
        self.signedInTable.setMinimumSize(QtCore.QSize(541, 691))
        self.signedInTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.signedInTable.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.signedInTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.signedInTable.setObjectName("signedInTable")
        self.signedInTable.setColumnCount(9)
        self.signedInTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.signedInTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.signedInTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.signedInTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.signedInTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.signedInTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.signedInTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.signedInTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.signedInTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.signedInTable.setHorizontalHeaderItem(8, item)
        self.signedInTable.verticalHeader().setDefaultSectionSize(40)
        self.signedInTable.verticalHeader().setMinimumSectionSize(40)
        self.verticalLayoutWidget = QtWidgets.QWidget(ManualSignOutPage)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(610, 319, 61, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addStudentButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addStudentButton.sizePolicy().hasHeightForWidth())
        self.addStudentButton.setSizePolicy(sizePolicy)
        self.addStudentButton.setMinimumSize(QtCore.QSize(50, 50))
        self.addStudentButton.setText("")
        self.addStudentButton.setObjectName("addStudentButton")
        self.verticalLayout.addWidget(self.addStudentButton)
        self.removeStudentButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeStudentButton.sizePolicy().hasHeightForWidth())
        self.removeStudentButton.setSizePolicy(sizePolicy)
        self.removeStudentButton.setMinimumSize(QtCore.QSize(45, 50))
        self.removeStudentButton.setText("")
        self.removeStudentButton.setObjectName("removeStudentButton")
        self.verticalLayout.addWidget(self.removeStudentButton)
        self.addAllStudentsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addAllStudentsButton.sizePolicy().hasHeightForWidth())
        self.addAllStudentsButton.setSizePolicy(sizePolicy)
        self.addAllStudentsButton.setMinimumSize(QtCore.QSize(50, 50))
        self.addAllStudentsButton.setText("")
        self.addAllStudentsButton.setObjectName("addAllStudentsButton")
        self.verticalLayout.addWidget(self.addAllStudentsButton)
        self.removeAllStudentsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeAllStudentsButton.sizePolicy().hasHeightForWidth())
        self.removeAllStudentsButton.setSizePolicy(sizePolicy)
        self.removeAllStudentsButton.setMinimumSize(QtCore.QSize(50, 50))
        self.removeAllStudentsButton.setText("")
        self.removeAllStudentsButton.setObjectName("removeAllStudentsButton")
        self.verticalLayout.addWidget(self.removeAllStudentsButton)
        self.signInPeriodGroupBox = QtWidgets.QGroupBox(ManualSignOutPage)
        self.signInPeriodGroupBox.setGeometry(QtCore.QRect(370, 860, 211, 81))
        self.signInPeriodGroupBox.setCheckable(True)
        self.signInPeriodGroupBox.setObjectName("signInPeriodGroupBox")
        self.hrsSpinbox = QtWidgets.QDoubleSpinBox(self.signInPeriodGroupBox)
        self.hrsSpinbox.setGeometry(QtCore.QRect(18, 34, 71, 35))
        self.hrsSpinbox.setMinimumSize(QtCore.QSize(69, 35))
        self.hrsSpinbox.setObjectName("hrsSpinbox")
        self.hrsLabel = QtWidgets.QLabel(self.signInPeriodGroupBox)
        self.hrsLabel.setGeometry(QtCore.QRect(100, 36, 67, 31))
        self.hrsLabel.setObjectName("hrsLabel")
        self.signOutTimeGroupBox = QtWidgets.QGroupBox(ManualSignOutPage)
        self.signOutTimeGroupBox.setGeometry(QtCore.QRect(700, 860, 211, 81))
        self.signOutTimeGroupBox.setCheckable(True)
        self.signOutTimeGroupBox.setObjectName("signOutTimeGroupBox")
        self.signOutTimeEdit = QtWidgets.QDateTimeEdit(self.signOutTimeGroupBox)
        self.signOutTimeEdit.setGeometry(QtCore.QRect(10, 29, 194, 40))
        self.signOutTimeEdit.setMinimumSize(QtCore.QSize(194, 40))
        self.signOutTimeEdit.setObjectName("signOutTimeEdit")
        self.orLabel = QtWidgets.QLabel(ManualSignOutPage)
        self.orLabel.setGeometry(QtCore.QRect(600, 870, 81, 51))
        self.orLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.orLabel.setObjectName("orLabel")

        self.retranslateUi(ManualSignOutPage)
        QtCore.QMetaObject.connectSlotsByName(ManualSignOutPage)

    def retranslateUi(self, ManualSignOutPage):
        _translate = QtCore.QCoreApplication.translate
        ManualSignOutPage.setWindowTitle(_translate("ManualSignOutPage", "Sign Out Students"))
        self.title.setText(_translate("ManualSignOutPage", "Sign Out"))
        self.closeButton.setText(_translate("ManualSignOutPage", "Close"))
        self.selectedStudentsGroupBox.setTitle(_translate("ManualSignOutPage", "Selected Students"))
        item = self.selectedTable.horizontalHeaderItem(0)
        item.setText(_translate("ManualSignOutPage", "Empl ID"))
        item = self.selectedTable.horizontalHeaderItem(1)
        item.setText(_translate("ManualSignOutPage", "Last Name"))
        item = self.selectedTable.horizontalHeaderItem(2)
        item.setText(_translate("ManualSignOutPage", "First Name"))
        item = self.selectedTable.horizontalHeaderItem(3)
        item.setText(_translate("ManualSignOutPage", "Course"))
        item = self.selectedTable.horizontalHeaderItem(4)
        item.setText(_translate("ManualSignOutPage", "Sign-In Time"))
        item = self.selectedTable.horizontalHeaderItem(5)
        item.setText(_translate("ManualSignOutPage", "Sign-Out Time"))
        item = self.selectedTable.horizontalHeaderItem(6)
        item.setText(_translate("ManualSignOutPage", "Service"))
        item = self.selectedTable.horizontalHeaderItem(7)
        item.setText(_translate("ManualSignOutPage", "Subject"))
        item = self.selectedTable.horizontalHeaderItem(8)
        item.setText(_translate("ManualSignOutPage", "Catalog"))
        item = self.selectedTable.horizontalHeaderItem(9)
        item.setText(_translate("ManualSignOutPage", "Section"))
        self.signOutButton.setText(_translate("ManualSignOutPage", "Sign Out Students"))
        self.signedInStudentsGroupBox.setTitle(_translate("ManualSignOutPage", "Signed In Students"))
        item = self.signedInTable.horizontalHeaderItem(0)
        item.setText(_translate("ManualSignOutPage", "Empl ID"))
        item = self.signedInTable.horizontalHeaderItem(1)
        item.setText(_translate("ManualSignOutPage", "Last Name"))
        item = self.signedInTable.horizontalHeaderItem(2)
        item.setText(_translate("ManualSignOutPage", "First Name"))
        item = self.signedInTable.horizontalHeaderItem(3)
        item.setText(_translate("ManualSignOutPage", "Course"))
        item = self.signedInTable.horizontalHeaderItem(4)
        item.setText(_translate("ManualSignOutPage", "Sign-In Time"))
        item = self.signedInTable.horizontalHeaderItem(5)
        item.setText(_translate("ManualSignOutPage", "Service"))
        item = self.signedInTable.horizontalHeaderItem(6)
        item.setText(_translate("ManualSignOutPage", "Subject"))
        item = self.signedInTable.horizontalHeaderItem(7)
        item.setText(_translate("ManualSignOutPage", "Catalog"))
        item = self.signedInTable.horizontalHeaderItem(8)
        item.setText(_translate("ManualSignOutPage", "Section"))
        self.signInPeriodGroupBox.setTitle(_translate("ManualSignOutPage", "Give a sign-in period of:"))
        self.hrsLabel.setText(_translate("ManualSignOutPage", "hrs"))
        self.signOutTimeGroupBox.setTitle(_translate("ManualSignOutPage", "Sign out at:"))
        self.orLabel.setText(_translate("ManualSignOutPage", "OR"))
