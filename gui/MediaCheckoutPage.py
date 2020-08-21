# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mediaCheckoutPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1109, 827)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(1000, 780, 101, 31))
        self.closeButton.setObjectName("closeButton")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 1091, 761))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.studentGridLayout = QtWidgets.QGridLayout()
        self.studentGridLayout.setObjectName("studentGridLayout")
        self.studentFirstNameLabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.studentFirstNameLabel.setObjectName("studentFirstNameLabel")
        self.studentGridLayout.addWidget(self.studentFirstNameLabel, 2, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.studentGridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label.setObjectName("label")
        self.studentGridLayout.addWidget(self.label, 2, 6, 1, 1)
        self.studentBarcodeInput = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.studentBarcodeInput.setReadOnly(True)
        self.studentBarcodeInput.setObjectName("studentBarcodeInput")
        self.studentGridLayout.addWidget(self.studentBarcodeInput, 3, 6, 1, 1)
        self.studentLastNameLabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.studentLastNameLabel.setObjectName("studentLastNameLabel")
        self.studentGridLayout.addWidget(self.studentLastNameLabel, 2, 2, 1, 1)
        self.studentLastNameInput = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentLastNameInput.sizePolicy().hasHeightForWidth())
        self.studentLastNameInput.setSizePolicy(sizePolicy)
        self.studentLastNameInput.setReadOnly(True)
        self.studentLastNameInput.setObjectName("studentLastNameInput")
        self.studentGridLayout.addWidget(self.studentLastNameInput, 3, 2, 1, 1)
        self.studentFirstNameInput = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentFirstNameInput.sizePolicy().hasHeightForWidth())
        self.studentFirstNameInput.setSizePolicy(sizePolicy)
        self.studentFirstNameInput.setReadOnly(True)
        self.studentFirstNameInput.setObjectName("studentFirstNameInput")
        self.studentGridLayout.addWidget(self.studentFirstNameInput, 3, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.studentGridLayout.addItem(spacerItem1, 4, 2, 1, 1)
        self.studentIDInput = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentIDInput.sizePolicy().hasHeightForWidth())
        self.studentIDInput.setSizePolicy(sizePolicy)
        self.studentIDInput.setReadOnly(True)
        self.studentIDInput.setObjectName("studentIDInput")
        self.studentGridLayout.addWidget(self.studentIDInput, 3, 5, 1, 1)
        self.studentIDLabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.studentIDLabel.setObjectName("studentIDLabel")
        self.studentGridLayout.addWidget(self.studentIDLabel, 2, 5, 1, 1)
        self.gridLayout.addLayout(self.studentGridLayout, 1, 0, 1, 1)
        self.tableLabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.tableLabel.setMinimumSize(QtCore.QSize(400, 17))
        self.tableLabel.setObjectName("tableLabel")
        self.gridLayout.addWidget(self.tableLabel, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.processButton = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.processButton.sizePolicy().hasHeightForWidth())
        self.processButton.setSizePolicy(sizePolicy)
        self.processButton.setMinimumSize(QtCore.QSize(120, 55))
        self.processButton.setBaseSize(QtCore.QSize(21, 16))
        self.processButton.setObjectName("processButton")
        self.gridLayout.addWidget(self.processButton, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.studentBorrowTable = QtWidgets.QTableWidget(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentBorrowTable.sizePolicy().hasHeightForWidth())
        self.studentBorrowTable.setSizePolicy(sizePolicy)
        self.studentBorrowTable.setMinimumSize(QtCore.QSize(979, 0))
        self.studentBorrowTable.setObjectName("studentBorrowTable")
        self.studentBorrowTable.setColumnCount(4)
        self.studentBorrowTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.studentBorrowTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentBorrowTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentBorrowTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentBorrowTable.setHorizontalHeaderItem(3, item)
        self.studentBorrowTable.horizontalHeader().setDefaultSectionSize(271)
        self.studentBorrowTable.horizontalHeader().setMinimumSectionSize(184)
        self.studentBorrowTable.horizontalHeader().setSortIndicatorShown(True)
        self.gridLayout.addWidget(self.studentBorrowTable, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mediaGridLayout = QtWidgets.QGridLayout()
        self.mediaGridLayout.setContentsMargins(-1, -1, 30, -1)
        self.mediaGridLayout.setObjectName("mediaGridLayout")
        self.mediaTitleInput = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.mediaTitleInput.setReadOnly(True)
        self.mediaTitleInput.setObjectName("mediaTitleInput")
        self.mediaGridLayout.addWidget(self.mediaTitleInput, 1, 1, 1, 1)
        self.mediaIDInput = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.mediaIDInput.setObjectName("mediaIDInput")
        self.mediaGridLayout.addWidget(self.mediaIDInput, 0, 1, 1, 1)
        self.mediaTypeLabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.mediaTypeLabel.setObjectName("mediaTypeLabel")
        self.mediaGridLayout.addWidget(self.mediaTypeLabel, 2, 0, 1, 1)
        self.mediaIDLabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.mediaIDLabel.setObjectName("mediaIDLabel")
        self.mediaGridLayout.addWidget(self.mediaIDLabel, 0, 0, 1, 1)
        self.mediaTypeInput = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.mediaTypeInput.setReadOnly(True)
        self.mediaTypeInput.setObjectName("mediaTypeInput")
        self.mediaGridLayout.addWidget(self.mediaTypeInput, 2, 1, 1, 1)
        self.mediaTitleLabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.mediaTitleLabel.setObjectName("mediaTitleLabel")
        self.mediaGridLayout.addWidget(self.mediaTitleLabel, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.mediaGridLayout)
        self.lookupGridLayout = QtWidgets.QGridLayout()
        self.lookupGridLayout.setContentsMargins(0, -1, 190, -1)
        self.lookupGridLayout.setHorizontalSpacing(10)
        self.lookupGridLayout.setVerticalSpacing(6)
        self.lookupGridLayout.setObjectName("lookupGridLayout")
        self.availableMediaButton = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.availableMediaButton.sizePolicy().hasHeightForWidth())
        self.availableMediaButton.setSizePolicy(sizePolicy)
        self.availableMediaButton.setMinimumSize(QtCore.QSize(120, 0))
        self.availableMediaButton.setObjectName("availableMediaButton")
        self.lookupGridLayout.addWidget(self.availableMediaButton, 1, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.outMediaButton = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outMediaButton.sizePolicy().hasHeightForWidth())
        self.outMediaButton.setSizePolicy(sizePolicy)
        self.outMediaButton.setMinimumSize(QtCore.QSize(120, 0))
        self.outMediaButton.setObjectName("outMediaButton")
        self.lookupGridLayout.addWidget(self.outMediaButton, 0, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.allMediaButton = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allMediaButton.sizePolicy().hasHeightForWidth())
        self.allMediaButton.setSizePolicy(sizePolicy)
        self.allMediaButton.setMinimumSize(QtCore.QSize(120, 0))
        self.allMediaButton.setObjectName("allMediaButton")
        self.lookupGridLayout.addWidget(self.allMediaButton, 2, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.lookupMediaLabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lookupMediaLabel.sizePolicy().hasHeightForWidth())
        self.lookupMediaLabel.setSizePolicy(sizePolicy)
        self.lookupMediaLabel.setMinimumSize(QtCore.QSize(176, 27))
        self.lookupMediaLabel.setLineWidth(1)
        self.lookupMediaLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lookupMediaLabel.setObjectName("lookupMediaLabel")
        self.lookupGridLayout.addWidget(self.lookupMediaLabel, 0, 1, 1, 1)
        self.horizontalLayout.addLayout(self.lookupGridLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Media Checkout"))
        self.closeButton.setText(_translate("MainWindow", "Close"))
        self.studentFirstNameLabel.setText(_translate("MainWindow", "Student First Name:"))
        self.label.setText(_translate("MainWindow", "Student Barcode:"))
        self.studentLastNameLabel.setText(_translate("MainWindow", "Student Last Name:"))
        self.studentIDLabel.setText(_translate("MainWindow", "Student ID:"))
        self.tableLabel.setText(_translate("MainWindow", "Student has:"))
        self.processButton.setText(_translate("MainWindow", "Process"))
        item = self.studentBorrowTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.studentBorrowTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.studentBorrowTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Type"))
        item = self.studentBorrowTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Time Out"))
        self.mediaTypeLabel.setText(_translate("MainWindow", "Media Type:"))
        self.mediaIDLabel.setText(_translate("MainWindow", "Media ID:"))
        self.mediaTitleLabel.setText(_translate("MainWindow", "Media Title:"))
        self.availableMediaButton.setText(_translate("MainWindow", "Available"))
        self.outMediaButton.setText(_translate("MainWindow", "Out"))
        self.allMediaButton.setText(_translate("MainWindow", "All"))
        self.lookupMediaLabel.setText(_translate("MainWindow", "Lookup Media:"))
