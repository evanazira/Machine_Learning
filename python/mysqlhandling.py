#you should not hardcode the data inside the program as follows
# fruits = ["apple","orange","mango"]
#you must keep apple,orange, mango in a txt file or csv file or exel file 
# write a python program to read the data
# 1) x to create the file if it does not exist
# 2) t file is going to be a text file
# 3) b is going to be a binary file
# 4) w let us write inside the file. 
#       But will clear the existing content inside the file.
# 5) a let us to append
#open ('fruit.txt', 'xt')


# #to open the exist file
# #method 1---------------------------------#
# import os
# os.path.exists('filename')
# #method 2---------------------------------#
# from os import path
# path.exists('filename')
#method 3--------------------------------#
from os.path import exists

# if exists(filename):
#     pass
# else:
#     open(filename, 'xt')

#---------------------------------------------------------------------#
import mysql.connector as mysql

def keyboardInput (datatype, caption, errorMessage, defaultValue = None):
    value = None
    isInvalid = True
    while (isInvalid):
        try:
            if defaultValue==None:
                value = datatype(input(caption))
            else:
                value = (input(caption))
                if value.strip()=="":
                    value = defaultValue
                else:
                    value = datatype(value)
        except:
            print(errorMessage)

        else:
            isInvalid = False

    return value
#-----------------------------------------------------------------------------#

def doMenu(connection):
    choice = -1

    while (choice != 0):
        print("\n\n")
        print("=================================")
        print("| 0 - Exit             |")
        print("| 1 - Print List       |")
        print("| 2 - Add              |")
        print("| 3 - Edit             |")
        print("| 4 - Delete           |")
        print("=================================")
        choice = keyboardInput(int, "Choice [0, 1, 2, 3, 4]: ", "Choice must be integer")
        print("\n\n")

        if choice== 0:
            print("Thank you for using our system")
        elif(choice==1):
            printProduct(connection)
        elif(choice==2):
            addProduct(connection)
        elif(choice==3):
             editProduct(connection)
        elif(choice==4):
             deleteProduct(connection)
#----------------------------------------------------------------------------#

def dbConnect():
    connection = mysql.connect(
        host = "localhost", user = "root", password = "", database = "peneraju")
    return connection
#---------------------------------------------------------------------------------#

def addProduct(connection):
    try:
        name = keyboardInput(str, "Product: ", "Product must be string")
        description = keyboardInput(str, "Description: ", "Description must be string")
        quantity = keyboardInput(int, "Quantity: ", "Quantity must be integer")
        price = keyboardInput(float, "Price: ", "Price must be float")
        SQL= f"""INSERT INTO products(name,description,quantity,price) VALUES('{name}','{description}',{quantity},{price})"""
        cursor = connection.cursor()
        cursor.execute(SQL)
        connection.commit()
        print("Product added successfully")

    except Exception as e:
        print("Something went wrong when we add the product: ", e)


#-------------------------------------------------------------------------------#

def printProduct(connection):
    # SQL = f"SELCT * FROM products"     #or
    SQL = f" SELECT id, name,description, quantity, price FROM products" 
  
    cursor = connection.cursor()
    cursor.execute(SQL)
    print("PRODUCT LIST")
    print("="*80)
    print(f"{'Id':6s} | {'Name':15s} | {'Description':30s} | {'Quantity':10s} | {'Price':10s}")
    
    for id,name,description,quantity,price in cursor:
        print(f"{id:6d} | {name:15s} | {description:30s} | {quantity:10d} | {price:10.2f}")
    print("="*80)

#---------------------------------------------------------------------------------#

def editProduct(connection):
    try:
        print("PRODUCT LIST")
        printProduct(connection)
        id = keyboardInput(int, "Please key in index of the product:", "Index must be integer")
        SQL = f"SELECT id, name, description, quantity, price FROM products WHERE id = {id}"
        cursor = connection.cursor()
        cursor.execute(SQL)
        id, name, description, quantity, price = cursor.fetchone()
    except:
        print("Product for thos ID does not exist")
    else:
        print(f"Product: {name}\nDescription: {description}\nQuantity: {quantity}\nPrice: {price}")
        confirm = keyboardInput(str," Are you sure you want to edit this product (y/n)?","Respond not valid")
        if (confirm=="y"):
            newproduct = keyboardInput(str, f"Product[{name}]: ", "Product must be string", name)
            newdescription = keyboardInput(str, f"Description[{description}]: ", "Desc must be str", description)
            newquantity = keyboardInput(int, f"Quantity[{quantity}]: ", "Quantity must be int", quantity)
            newprice = keyboardInput(float, f"Price[{price}]: ", "Price must be float", price)
            SQL = f"""UPDATE products SET name = '{newproduct}',description = '{newdescription}',quantity = {newquantity},price = {newprice} WHERE id = {id}"""
            cursor = connection.cursor()
            cursor.execute(SQL)
            connection.commit()
#----------------------------------------------------------------------------------------#

def deleteProduct(connection):
    try:
        print("PRODUCT LIST")
        printProduct(connection)
        id = keyboardInput(int, "Please key in index of the product:", "Index must be integer")
        SQL = f"SELECT id, name, description, quantity, price FROM products WHERE id = {id}"
        cursor = connection.cursor()
        cursor.execute(SQL)
        id, name, description, quantity, price = cursor.fetchone()
    except:
        print("Product for thos ID does not exist")
    else:
        print(f"Product: {name}\nDescription: {description}\nQuantity: {quantity}\nPrice: {price}")
        confirm = keyboardInput(str," Are you sure you want to delete this product (y/n)?","Respond not valid")
        if (confirm=="y"):
            SQL = f""" DELETE FROM products WHERE id= {id}"""
            cursor = connection.cursor()
            cursor.execute(SQL)
            connection.commit()

#--------------------------------------------------------------------------------------#

connection = dbConnect()
doMenu(connection)
#addProduct(filename)
#printProduct (filename)
