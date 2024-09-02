import sys
import mysql.connector
from DispProducts import *
from PyQt5 import QtWidgets, QtCore

def createConnection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Th00l$122",
            database="shopping"
        )
        if conn.is_connected():
            print("Connected to MySQL database")
            return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

class MyForm(QtWidgets.QDialog):
    recno = 0

    def __init__(self, conn, parent=None):
        super(MyForm, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.conn = conn
        self.cursor = self.conn.cursor()

        self.loadData()
        self.updateFields()

        self.ui.FirstButton.clicked.connect(self.dispFirst)
        self.ui.PreviousButton.clicked.connect(self.dispPrevious)
        self.ui.LastButton.clicked.connect(self.dispLast)
        self.ui.NextButton.clicked.connect(self.dispNext)

    def loadData(self):
        self.cursor.execute("SELECT * FROM products")
        self.records = self.cursor.fetchall()

    def updateFields(self):
        record = self.records[MyForm.recno]
        self.ui.prodid.setText(str(record[0]))
        self.ui.prodname.setText(record[1])
        self.ui.qty.setText(str(record[2]))
        self.ui.price.setText(str(record[3]))

    def dispFirst(self):
        MyForm.recno = 0
        self.updateFields()

    def dispPrevious(self):
        MyForm.recno -= 1
        if MyForm.recno < 0:
            MyForm.recno = len(self.records) - 1
        self.updateFields()

    def dispLast(self):
        MyForm.recno = len(self.records) - 1
        self.updateFields()

    def dispNext(self):
        MyForm.recno += 1
        if MyForm.recno >= len(self.records):
            MyForm.recno = 0
        self.updateFields()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    conn = createConnection()
    if not conn:
        sys.exit(1)
    myapp = MyForm(conn)
    myapp.show()
    sys.exit(app.exec_())




#To retrieve from thedatabase table, you use a static variable, recno. The recno variable is initially set to 0 to
#display the first row. When you select Next, the value of the variable recnois incremented by
#1 to display the next row. If the user selects Next on the last row of the table, the value of the recnovariable is reset to 0 to display the first row.


   
