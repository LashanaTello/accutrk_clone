# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coursesPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CoursesPage(object):
    def setupUi(self, CoursesPage):
        CoursesPage.setObjectName("CoursesPage")
        CoursesPage.resize(1092, 927)
        self.coursesTable = QtWidgets.QTableWidget(CoursesPage)
        self.coursesTable.setGeometry(QtCore.QRect(10, 160, 941, 711))
        self.coursesTable.setAutoScrollMargin(16)
        self.coursesTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.coursesTable.setObjectName("coursesTable")
        self.coursesTable.setColumnCount(6)
        self.coursesTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.coursesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.coursesTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.coursesTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.coursesTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.coursesTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.coursesTable.setHorizontalHeaderItem(5, item)
        self.coursesTable.horizontalHeader().setDefaultSectionSize(146)
        self.coursesTable.horizontalHeader().setMinimumSectionSize(146)
        self.coursesTable.horizontalHeader().setStretchLastSection(True)
        self.coursesTable.verticalHeader().setDefaultSectionSize(45)
        self.coursesTable.verticalHeader().setMinimumSectionSize(45)
        self.verticalLayoutWidget = QtWidgets.QWidget(CoursesPage)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(958, 230, 121, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.editButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.editButton.setMinimumSize(QtCore.QSize(97, 50))
        self.editButton.setObjectName("editButton")
        self.verticalLayout.addWidget(self.editButton)
        self.deleteButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.deleteButton.setMinimumSize(QtCore.QSize(97, 50))
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout.addWidget(self.deleteButton)
        self.registrationButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.registrationButton.setMinimumSize(QtCore.QSize(97, 50))
        self.registrationButton.setObjectName("registrationButton")
        self.verticalLayout.addWidget(self.registrationButton)
        self.horizontalLayoutWidget = QtWidgets.QWidget(CoursesPage)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 870, 181, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.classesLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.classesLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.classesLabel.setObjectName("classesLabel")
        self.horizontalLayout.addWidget(self.classesLabel)
        self.numCoursesLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.numCoursesLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.numCoursesLabel.setObjectName("numCoursesLabel")
        self.horizontalLayout.addWidget(self.numCoursesLabel)
        self.gridLayoutWidget = QtWidgets.QWidget(CoursesPage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1071, 134))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.refreshButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.refreshButton.setMinimumSize(QtCore.QSize(96, 35))
        self.refreshButton.setObjectName("refreshButton")
        self.gridLayout.addWidget(self.refreshButton, 2, 3, 1, 1)
        self.addButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.addButton.setMinimumSize(QtCore.QSize(97, 35))
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 2, 4, 1, 1)
        self.searchImage = QtWidgets.QLabel(self.gridLayoutWidget)
        self.searchImage.setMinimumSize(QtCore.QSize(42, 35))
        self.searchImage.setObjectName("searchImage")
        self.gridLayout.addWidget(self.searchImage, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.searchbar = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchbar.sizePolicy().hasHeightForWidth())
        self.searchbar.setSizePolicy(sizePolicy)
        self.searchbar.setMinimumSize(QtCore.QSize(500, 35))
        self.searchbar.setObjectName("searchbar")
        self.gridLayout.addWidget(self.searchbar, 2, 1, 1, 1)
        self.searchByComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.searchByComboBox.setMinimumSize(QtCore.QSize(150, 35))
        self.searchByComboBox.setMaxVisibleItems(6)
        self.searchByComboBox.setMaxCount(6)
        self.searchByComboBox.setObjectName("searchByComboBox")
        self.searchByComboBox.addItem("")
        self.searchByComboBox.addItem("")
        self.searchByComboBox.addItem("")
        self.searchByComboBox.addItem("")
        self.searchByComboBox.addItem("")
        self.searchByComboBox.addItem("")
        self.gridLayout.addWidget(self.searchByComboBox, 2, 2, 1, 1)
        self.closeButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.closeButton.setMinimumSize(QtCore.QSize(97, 45))
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 0, 5, 1, 1)
        self.titleLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.titleLabel.setMinimumSize(QtCore.QSize(62, 40))
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout.addWidget(self.titleLabel, 1, 0, 1, 2, QtCore.Qt.AlignRight)

        self.retranslateUi(CoursesPage)
        self.searchByComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CoursesPage)

    def retranslateUi(self, CoursesPage):
        _translate = QtCore.QCoreApplication.translate
        CoursesPage.setWindowTitle(_translate("CoursesPage", "Courses"))
        item = self.coursesTable.horizontalHeaderItem(0)
        item.setText(_translate("CoursesPage", "Subject"))
        item = self.coursesTable.horizontalHeaderItem(1)
        item.setText(_translate("CoursesPage", "Catalog"))
        item = self.coursesTable.horizontalHeaderItem(2)
        item.setText(_translate("CoursesPage", "Section"))
        item = self.coursesTable.horizontalHeaderItem(3)
        item.setText(_translate("CoursesPage", "# of Students"))
        item = self.coursesTable.horizontalHeaderItem(4)
        item.setText(_translate("CoursesPage", "Professor"))
        item = self.coursesTable.horizontalHeaderItem(5)
        item.setText(_translate("CoursesPage", "Professor Email"))
        self.editButton.setText(_translate("CoursesPage", "edit"))
        self.deleteButton.setText(_translate("CoursesPage", "delete"))
        self.registrationButton.setText(_translate("CoursesPage", "registration list"))
        self.classesLabel.setText(_translate("CoursesPage", "Courses"))
        self.numCoursesLabel.setText(_translate("CoursesPage", "0"))
        self.refreshButton.setText(_translate("CoursesPage", "refresh"))
        self.addButton.setText(_translate("CoursesPage", "add"))
        self.searchImage.setText(_translate("CoursesPage", "image"))
        self.searchByComboBox.setCurrentText(_translate("CoursesPage", "Subject"))
        self.searchByComboBox.setItemText(0, _translate("CoursesPage", "Subject"))
        self.searchByComboBox.setItemText(1, _translate("CoursesPage", "Catalog"))
        self.searchByComboBox.setItemText(2, _translate("CoursesPage", "Section"))
        self.searchByComboBox.setItemText(3, _translate("CoursesPage", "# of Students"))
        self.searchByComboBox.setItemText(4, _translate("CoursesPage", "Professor"))
        self.searchByComboBox.setItemText(5, _translate("CoursesPage", "Professor Email"))
        self.closeButton.setText(_translate("CoursesPage", "close"))
        self.titleLabel.setText(_translate("CoursesPage", "Courses"))
