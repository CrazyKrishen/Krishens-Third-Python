import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtCore
from addInHorizontalLayout import Ui_Dialog

class MyForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.dispsum)
        self.ui.pushButton_2.clicked.connect(self.reject)

    def reject(self):
        self.close()

    def dispsum(self):
        try:
            a = int(self.ui.lineEdit.text()) if self.ui.lineEdit.text() else 0
            b = int(self.ui.lineEdit_2.text()) if self.ui.lineEdit_2.text() else 0
            sum = a + b
            self.ui.label_3.setText(f"Addition: {sum}")
        except ValueError:
            self.ui.label_3.setText("Invalid input")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
