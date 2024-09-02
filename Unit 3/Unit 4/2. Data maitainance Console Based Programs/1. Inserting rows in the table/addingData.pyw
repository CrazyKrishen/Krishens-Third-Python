import sys
import mysql.connector


conn = mysql.connector.connect(host="localhost", user="root", passwd="Th00l$122", database="Shopping")  #the database shopping was already created
myCursor = conn.cursor() #creating the cursor using conn after esablishing a connectoion

try:
    myCursor.execute("""
    insert into products(prod_id, prod_name, quantity, price)
    VALUES (101,'Camera', 100, 15)
""")
    conn.commit() #saving the data inserted
    print('A row was inserted.')
except:
    conn.rollback()   #The rollback()method cancels all the modifications applied to the database table. It keeps the database table at the state it was when it was last saved.

myCursor.close()
conn.close()

    
