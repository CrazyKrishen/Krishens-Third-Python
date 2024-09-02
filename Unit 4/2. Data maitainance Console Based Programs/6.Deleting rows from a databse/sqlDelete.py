import sys
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="Th00l$122", database="shopping")
myCursor = conn.cursor()

prodIDDel = int(input("Please enter the product ID to delete: "))

myCursor.execute("SELECT * FROM products where prod_id= %s", (prodIDDel,)) #executing the command on sql
row = myCursor.fetchone()  #fetching all rows with that ID

if row==None:
    print("No products ID %d is found " %prodIDDel)
else:
    print("Information of ID %d is as follows:" % prodIDDel)
    print ("Product ID: %d, Product Name: %s, Quantity: %d, Price: %f" %(row[0],row[1],row[2],row[3]))
    print("")

    confirm = input("You sure you want to delete ID %d: " % prodIDDel)
    answer = confirm.upper()

    if answer == "YES":
        myCursor.execute("DELETE from products where prod_id= %s", (prodIDDel,))
        print("Product ID %d is deleted." % prodIDDel)
        conn.commit()
    else:
        print("Deletion aborted!")

myCursor.close()
conn.close()
