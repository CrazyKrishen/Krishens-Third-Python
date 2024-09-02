import sys
import mysql.connector


conn = mysql.connector.connect(host="localhost", user="root", passwd="Th00l$122", database="Shopping")  #the database shopping was already created
myCursor = conn.cursor() #creating the cursor using conn after esablishing a connectoion

answer = "YES"
while answer.upper() =="YES":
    prodID = int(input("Enter product ID: "))
    prodName = input("Enter product name: ")
    prodQuantity = int(input("Enter product quantity: "))
    prodPrice = int(input("Enter product ptice R: "))

    try:
        myCursor.execute("""
        INSERT INTO products(prod_id, prod_name, quantity, price)
        VALUES(%d, '%s', %d, %f)
        """ %(prodID, prodName, prodQuantity, prodPrice))
        conn.commit()
        print("Saved!")
        userAnswer = input("Want to insert more products, yes/no: ")
        answer = userAnswer.upper()
    except:
        conn.rollback
        sys.exit(1)


myCursor.close()
conn.close()


#Next go to The command line prompt and type in:
#select * from products;
#The table will pop up with all the data entered
