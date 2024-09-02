import sys
import mysql.connector


conn = mysql.connector.connect(host="localhost", user="root", passwd="Th00l$122", database="Shopping")  #the database shopping was already created
myCursor = conn.cursor() #creating the cursor using conn after esablishing a connectoion

try:
    myCursor.execute("SELECT * from products")
    print("Product ID\tProduct Name\tQuantity\tPrice(R)")
    while(1):
        row = myCursor.fetchone()
        if row==None:
            break
        print("%d\t\t%s\t\t%d\t\t%f" % (row[0], row[1], row[2], row[3]))

except mysql.connector.Error:
    print("Errir ub fetching rows")
    sys.exit(1)


myCursor.close()
conn.close()



#This program explains how to use the fetchone()method to fetch rows from a database table.

#Now let’s use another method, fetchall(), for retrieving and displaying all rows of a database table.
