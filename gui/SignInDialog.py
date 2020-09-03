# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signInDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignInDialog(object):
    def setupUi(self, SignInDialog):
        SignInDialog.setObjectName("SignInDialog")
        SignInDialog.resize(698, 940)
        self.gridLayoutWidget = QtWidgets.QWidget(SignInDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 100, 591, 831))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.classLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.classLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.classLabel.setObjectName("classLabel")
        self.gridLayout.addWidget(self.classLabel, 7, 0, 1, 3)
        self.eventLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eventLabel.sizePolicy().hasHeightForWidth())
        self.eventLabel.setSizePolicy(sizePolicy)
        self.eventLabel.setMinimumSize(QtCore.QSize(254, 18))
        self.eventLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.eventLabel.setObjectName("eventLabel")
        self.gridLayout.addWidget(self.eventLabel, 3, 0, 1, 3)
        self.classTable = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.classTable.setMinimumSize(QtCore.QSize(425, 192))
        self.classTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.classTable.setAlternatingRowColors(True)
        self.classTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.classTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.classTable.setShowGrid(True)
        self.classTable.setObjectName("classTable")
        self.classTable.setColumnCount(3)
        self.classTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setHorizontalHeaderItem(2, item)
        self.classTable.horizontalHeader().setDefaultSectionSize(136)
        self.classTable.horizontalHeader().setMinimumSectionSize(136)
        self.gridLayout.addWidget(self.classTable, 8, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.semesterList = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.semesterList.setObjectName("semesterList")
        self.gridLayout.addWidget(self.semesterList, 2, 0, 1, 1)
        self.serviceList = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.serviceList.setObjectName("serviceList")
        self.gridLayout.addWidget(self.serviceList, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)
        self.cancelButton.setMinimumSize(QtCore.QSize(100, 42))
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 10, 0, 1, 1, QtCore.Qt.AlignRight)
        self.semesterLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.semesterLabel.sizePolicy().hasHeightForWidth())
        self.semesterLabel.setSizePolicy(sizePolicy)
        self.semesterLabel.setMinimumSize(QtCore.QSize(254, 20))
        self.semesterLabel.setObjectName("semesterLabel")
        self.gridLayout.addWidget(self.semesterLabel, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem2, 9, 0, 1, 3)
        self.eventList = QtWidgets.QListWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eventList.sizePolicy().hasHeightForWidth())
        self.eventList.setSizePolicy(sizePolicy)
        self.eventList.setMinimumSize(QtCore.QSize(435, 116))
        self.eventList.setObjectName("eventList")
        item = QtWidgets.QListWidgetItem()
        self.eventList.addItem(item)
        self.gridLayout.addWidget(self.eventList, 5, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.serviceLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serviceLabel.sizePolicy().hasHeightForWidth())
        self.serviceLabel.setSizePolicy(sizePolicy)
        self.serviceLabel.setMinimumSize(QtCore.QSize(254, 20))
        self.serviceLabel.setObjectName("serviceLabel")
        self.gridLayout.addWidget(self.serviceLabel, 0, 2, 1, 1)
        self.signInButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signInButton.sizePolicy().hasHeightForWidth())
        self.signInButton.setSizePolicy(sizePolicy)
        self.signInButton.setMinimumSize(QtCore.QSize(100, 42))
        self.signInButton.setObjectName("signInButton")
        self.gridLayout.addWidget(self.signInButton, 10, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(SignInDialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(210, 20, 391, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 15, 0)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.studentEIDLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentEIDLabel.sizePolicy().hasHeightForWidth())
        self.studentEIDLabel.setSizePolicy(sizePolicy)
        self.studentEIDLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.studentEIDLabel.setObjectName("studentEIDLabel")
        self.gridLayout_2.addWidget(self.studentEIDLabel, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.studentNameLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentNameLabel.sizePolicy().hasHeightForWidth())
        self.studentNameLabel.setSizePolicy(sizePolicy)
        self.studentNameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.studentNameLabel.setObjectName("studentNameLabel")
        self.gridLayout_2.addWidget(self.studentNameLabel, 2, 1, 1, 1)
        self.studentBarcodeLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentBarcodeLabel.sizePolicy().hasHeightForWidth())
        self.studentBarcodeLabel.setSizePolicy(sizePolicy)
        self.studentBarcodeLabel.setMinimumSize(QtCore.QSize(140, 0))
        self.studentBarcodeLabel.setBaseSize(QtCore.QSize(17, 0))
        self.studentBarcodeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.studentBarcodeLabel.setObjectName("studentBarcodeLabel")
        self.gridLayout_2.addWidget(self.studentBarcodeLabel, 1, 1, 1, 1)

        self.retranslateUi(SignInDialog)
        QtCore.QMetaObject.connectSlotsByName(SignInDialog)

    def retranslateUi(self, SignInDialog):
        _translate = QtCore.QCoreApplication.translate
        SignInDialog.setWindowTitle(_translate("SignInDialog", "Sign In"))
        self.classLabel.setText(_translate("SignInDialog", "Class"))
        self.eventLabel.setText(_translate("SignInDialog", "Events"))
        item = self.classTable.horizontalHeaderItem(0)
        item.setText(_translate("SignInDialog", "Subject"))
        item = self.classTable.horizontalHeaderItem(1)
        item.setText(_translate("SignInDialog", "Catalog"))
        item = self.classTable.horizontalHeaderItem(2)
        item.setText(_translate("SignInDialog", "Section"))
        self.cancelButton.setText(_translate("SignInDialog", "Cancel"))
        self.semesterLabel.setText(_translate("SignInDialog", "Semester"))
        __sortingEnabled = self.eventList.isSortingEnabled()
        self.eventList.setSortingEnabled(False)
        item = self.eventList.item(0)
        item.setText(_translate("SignInDialog", "example"))
        self.eventList.setSortingEnabled(__sortingEnabled)
        self.serviceLabel.setText(_translate("SignInDialog", "Service"))
        self.signInButton.setText(_translate("SignInDialog", "Sign In"))
        self.label.setText(_translate("SignInDialog", "ID:"))
        self.label_2.setText(_translate("SignInDialog", "Barcode:"))
        self.studentEIDLabel.setText(_translate("SignInDialog", "studentID"))
        self.label_3.setText(_translate("SignInDialog", "Name:"))
        self.studentNameLabel.setText(_translate("SignInDialog", "studentName"))
        self.studentBarcodeLabel.setText(_translate("SignInDialog", "studentBarcode"))
