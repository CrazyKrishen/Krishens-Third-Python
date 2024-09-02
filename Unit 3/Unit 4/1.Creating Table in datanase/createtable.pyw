#A database is a collection of information that is organized so that it can easily be accessed,managed, and updated. Its like a hard drive
#that you can add tables with their cols and rows and indexes etc...

#I have already created a database called 'shopping'. Now we creating tables in the database.
import sys
import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root", passwd="Th00l$122",database="shopping")
myCursor = conn.cursor()

try:
    myCursor.execute("""
    create table products(
    prod_id smallint NOT NULL,
    prod_name char(50),
    quantity smallint,
    price float
    )
""")
    print("Table 'products' created successfully.")
    
except mysql.connector.Error:
    print("Error in creating products table")
    sys.exit(1)
    myCursor.close()
    conn.close()
    

#This video below will help you understand how to create a cursor
#https://www.youtube.com/watch?v=3vsC05rxZ8c


#connect(): means you indicate that you want to connect to the shopping database via the authorized user, root.


#aftercreating the table here go to SQL Commandline and enter the following step by step:
#use database_name;    this loads the database you want to use
#show tables;         #this shows all the tables in that particular database
#describe tabe_name;    #this will show all the columns and they data types in that table
