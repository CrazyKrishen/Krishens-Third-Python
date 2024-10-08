# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groupbox.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(628, 568)
        Dialog.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 331, 531))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.vanilla = QtWidgets.QRadioButton(self.groupBox)
        self.vanilla.setGeometry(QtCore.QRect(20, 40, 141, 20))
        self.vanilla.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.vanilla.setObjectName("vanilla")
        self.blacksunday = QtWidgets.QRadioButton(self.groupBox)
        self.blacksunday.setGeometry(QtCore.QRect(20, 80, 161, 20))
        self.blacksunday.setObjectName("blacksunday")
        self.chocolatechips = QtWidgets.QRadioButton(self.groupBox)
        self.chocolatechips.setGeometry(QtCore.QRect(20, 120, 191, 20))
        self.chocolatechips.setObjectName("chocolatechips")
        self.strawberry = QtWidgets.QRadioButton(self.groupBox)
        self.strawberry.setGeometry(QtCore.QRect(20, 160, 151, 20))
        self.strawberry.setObjectName("strawberry")
        self.verticalLayout.addWidget(self.groupBox)
        self.DrinkBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.DrinkBox.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.DrinkBox.setCheckable(True)
        self.DrinkBox.setObjectName("DrinkBox")
        self.coffee = QtWidgets.QRadioButton(self.DrinkBox)
        self.coffee.setGeometry(QtCore.QRect(20, 40, 95, 20))
        self.coffee.setObjectName("coffee")
        self.colddrink = QtWidgets.QRadioButton(self.DrinkBox)
        self.colddrink.setGeometry(QtCore.QRect(20, 80, 131, 20))
        self.colddrink.setObjectName("colddrink")
        self.juice = QtWidgets.QRadioButton(self.DrinkBox)
        self.juice.setGeometry(QtCore.QRect(20, 130, 95, 20))
        self.juice.setObjectName("juice")
        self.verticalLayout.addWidget(self.DrinkBox)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(370, 32, 171, 351))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 188, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 88, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.calculateButton = QtWidgets.QPushButton(self.widget)
        self.calculateButton.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.calculateButton.setObjectName("calculateButton")
        self.gridLayout.addWidget(self.calculateButton, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Ice Cream"))
        self.vanilla.setText(_translate("Dialog", " Plain Vanilla R50"))
        self.blacksunday.setText(_translate("Dialog", "Black Sunday R100"))
        self.chocolatechips.setText(_translate("Dialog", " Chocolate Chips R200"))
        self.strawberry.setText(_translate("Dialog", "Strawberry R150"))
        self.DrinkBox.setTitle(_translate("Dialog", "Drinks"))
        self.coffee.setText(_translate("Dialog", "Coffee R50"))
        self.colddrink.setText(_translate("Dialog", "Cold Drink R100"))
        self.juice.setText(_translate("Dialog", " Juice R150"))
        self.calculateButton.setText(_translate("Dialog", "Calculate Bill"))
