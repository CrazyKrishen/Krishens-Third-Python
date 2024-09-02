#updating information alreaady stored on the table 
import sys
import mysql.connector


conn = mysql.connector.connect(host="localhost", user="root", passwd="Th00l$122", database="Shopping")  #the database shopping was already created
myCursor = conn.cursor() #creating the cursor using conn after esablishing a connectoion

prodID = int(input("Enter product ID: "))
myCursor.execute("SELECT * from products where prod_id= %d" %prodID)
row = myCursor.fetchone()

if row == None:
    print("Sorry no Product found with ID %d" %prodID)
else:
    print("Information of the product with ID %d is as follows: " %prodID)
    print ("Product ID: %d, Product Name: %s, Quantity: %d, Proce: %f" %(row[0],row[1],row[2],row[3]))
    print(" ")
    
    newPName = input("Enter new product name: ")
    newPQuantity = int(input("Enter new product quantity: "))
    newPPrice = int(input("Enter new price: "))
    myCursor.execute("UPDATE products SET prod_name = %s, quantity = %s, price = %s WHERE prod_id = %s",(newPName, newPQuantity, newPPrice, prodID))  
    conn.commit()
    print(" ")

    #fetching updated information
    myCursor.execute("SELECT * FROM products WHERE prod_id = %s", (prodID,))
    updated_row = myCursor.fetchone()
    
    print("THE UPDATED INOFORMATION FOR PRODUCT ID %d is " %prodID)
    print("Product ID: %d, Product Name: %s, Quantity: %d, Price: %f" % (updated_row[0], updated_row[1], updated_row[2], updated_row[3]))


myCursor.close()
conn.close()


# notice that in any myCursor.execute(), for paramterized calling of data, it all has %s no matter the data type
# the data type only matters in the print statement, so meaning thats when you use %d %s %f
