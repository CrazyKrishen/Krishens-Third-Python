# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MaintainProducts.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1005, 693)
        Dialog.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 60, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.label.setObjectName("label")
        self.prodname = QtWidgets.QLineEdit(Dialog)
        self.prodname.setGeometry(QtCore.QRect(240, 61, 321, 31))
        self.prodname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.prodname.setObjectName("prodname")
        self.FilterButton = QtWidgets.QPushButton(Dialog)
        self.FilterButton.setGeometry(QtCore.QRect(610, 60, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.FilterButton.setFont(font)
        self.FilterButton.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.FilterButton.setObjectName("FilterButton")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(30, 110, 931, 401))
        self.tableView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableView.setObjectName("tableView")
        self.UpdateButton = QtWidgets.QPushButton(Dialog)
        self.UpdateButton.setGeometry(QtCore.QRect(90, 560, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.UpdateButton.setFont(font)
        self.UpdateButton.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.UpdateButton.setObjectName("UpdateButton")
        self.CancelButton = QtWidgets.QPushButton(Dialog)
        self.CancelButton.setGeometry(QtCore.QRect(310, 560, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CancelButton.setFont(font)
        self.CancelButton.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.CancelButton.setObjectName("CancelButton")
        self.InsertButton = QtWidgets.QPushButton(Dialog)
        self.InsertButton.setGeometry(QtCore.QRect(530, 560, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.InsertButton.setFont(font)
        self.InsertButton.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.InsertButton.setObjectName("InsertButton")
        self.DeleteButton = QtWidgets.QPushButton(Dialog)
        self.DeleteButton.setGeometry(QtCore.QRect(710, 560, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DeleteButton.setFont(font)
        self.DeleteButton.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.DeleteButton.setObjectName("DeleteButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Product Name"))
        self.FilterButton.setText(_translate("Dialog", "Filter"))
        self.UpdateButton.setText(_translate("Dialog", "Update"))
        self.CancelButton.setText(_translate("Dialog", "Cancel"))
        self.InsertButton.setText(_translate("Dialog", "Add"))
        self.DeleteButton.setText(_translate("Dialog", "Delete"))
