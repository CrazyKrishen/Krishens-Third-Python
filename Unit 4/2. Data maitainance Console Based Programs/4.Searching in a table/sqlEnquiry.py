#fetching all products from the table
#Now this program fetches all information with that particular ID entered by the user 
import sys
import mysql.connector


conn = mysql.connector.connect(host="localhost", user="root", passwd="Th00l$122", database="Shopping")  #the database shopping was already created
myCursor = conn.cursor() #creating the cursor using conn after esablishing a connectoion

prodID = int(input("Enter Product ID: "))
myCursor.execute("SELECT * FROM products where prod_id =%d" %prodID)
row = myCursor.fetchone()

if row == None:
    print("No row product found with ID %d" %prodID)
else:
    print ("Information of the product with ID %d is as follows:" %prodID)
    print ("Product ID: %d, Product Name: %s, Quantity: %d, Price: %f" %(row[0],row[1],row[2],row[3]))


myCursor.close()
conn.close()
