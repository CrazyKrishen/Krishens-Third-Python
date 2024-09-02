#in this program we are reading whats on the database and displaying it here
import sys
import mysql.connector
from showrec import *
from PyQt5 import QtWidgets, QtGui, QtCore

def createConnection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Th00l$122",
            database="shopping"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

class MyForm(QtWidgets.QDialog):
    def __init__(self, conn, parent=None):
        super(MyForm, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.conn = conn
        self.populateTableView()

    def populateTableView(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()

        # Creating a QStandardItemModel to hold the data
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(["Product ID", "Product Name", "Quantity", "Price"])

        for row in rows:
            items = [
                QtGui.QStandardItem(str(row[0])),
                QtGui.QStandardItem(row[1]),
                QtGui.QStandardItem(str(row[2])),
                QtGui.QStandardItem(str(row[3]))
            ]
            model.appendRow(items)

        # Use the correct widget name (treeView or tableView)
        self.ui.treeView.setModel(model)
        cursor.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    conn = createConnection()
    if conn is None:
        sys.exit(1)
    myapp = MyForm(conn)
    myapp.show()
    sys.exit(app.exec_())
    conn.close()
