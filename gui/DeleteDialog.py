# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeleteDialog(object):
    def setupUi(self, DeleteDialog):
        DeleteDialog.setObjectName("DeleteDialog")
        DeleteDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        DeleteDialog.resize(480, 199)
        self.message = QtWidgets.QLabel(DeleteDialog)
        self.message.setGeometry(QtCore.QRect(20, 30, 321, 35))
        self.message.setMinimumSize(QtCore.QSize(120, 35))
        self.message.setObjectName("message")
        self.nameLabel = QtWidgets.QLabel(DeleteDialog)
        self.nameLabel.setGeometry(QtCore.QRect(20, 80, 441, 35))
        self.nameLabel.setMinimumSize(QtCore.QSize(250, 35))
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.cancelButton = QtWidgets.QPushButton(DeleteDialog)
        self.cancelButton.setGeometry(QtCore.QRect(70, 140, 131, 35))
        self.cancelButton.setMinimumSize(QtCore.QSize(131, 35))
        self.cancelButton.setObjectName("cancelButton")
        self.deleteButton = QtWidgets.QPushButton(DeleteDialog)
        self.deleteButton.setGeometry(QtCore.QRect(270, 140, 131, 35))
        self.deleteButton.setMinimumSize(QtCore.QSize(131, 35))
        self.deleteButton.setObjectName("deleteButton")

        self.retranslateUi(DeleteDialog)
        QtCore.QMetaObject.connectSlotsByName(DeleteDialog)

    def retranslateUi(self, DeleteDialog):
        _translate = QtCore.QCoreApplication.translate
        DeleteDialog.setWindowTitle(_translate("DeleteDialog", "Delete Student?"))
        self.message.setText(_translate("DeleteDialog", "Are you sure you want to delete this student?"))
        self.nameLabel.setText(_translate("DeleteDialog", "blank"))
        self.cancelButton.setText(_translate("DeleteDialog", "Cancel"))
        self.deleteButton.setText(_translate("DeleteDialog", "Delete Student"))
