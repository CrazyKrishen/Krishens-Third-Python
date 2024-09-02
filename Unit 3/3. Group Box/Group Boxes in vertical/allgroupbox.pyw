import sys
from PyQt5 import QtWidgets, QtCore
from groupbox import Ui_Dialog

class MyForm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.calculateButton.clicked.connect(self.calculatebill)

    def calculatebill(self):
        bill = 0

        if self.ui.vanilla.isChecked():
            bill += 50

        if self.ui.blacksunday.isChecked():
            bill += 100

        if self.ui.chocolatechips.isChecked():
            bill += 200

        if self.ui.strawberry.isChecked():
            bill += 150

        if self.ui.DrinkBox.isChecked():
            if self.ui.coffee.isChecked():
                bill += 50

            if self.ui.colddrink.isChecked():
                bill += 100

            if self.ui.juice.isChecked():
                bill += 150

        self.ui.label.setText("The bill is: R" + str(bill))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
            
