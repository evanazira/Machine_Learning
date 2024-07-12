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

def doMenu(filename):
    choice = -1

    while (choice != 0):
        print("\n\n")
        print("=================================")
        print("| 0 - Exit                      |")
        print("| 1 - Cars Insurance List       |")
        print("| 2 - Drivers Insurance List    |")
        print("| 3 - Insurance Claim           |")
        print("| 4 - Overall Insurance Report  |")
        print("=================================")
        choice = keyboardInput(int, "Choice [0, 1, 2, 3, 4]: ", "Choice must be integer")
        print("\n\n")

        if choice== 0:
            print("Thank you for using our system")
        elif(choice==1):
            carList(filename)
        elif(choice==2):
            driverList(filename)
        elif(choice==3):
             insuranceClaim(filename)
        elif(choice==4):
             overallReport(filename)
#----------------------------------------------------------------------------#

def createFile(filename):
    if not exists(filename):
        try:
            #filehandler is an object/instance of File class
            filehandler = open(filename, "xt")

        except Exception as e:
            print("Something went wrong when we create the file: ", e)

        else:
            #only if the file open is succussful, this will execute
            createTitle(filename)


        finally:
            #filehandler has many methods like read, write, and close
            #close is a method in the open class
            filehandler.close()





#whenever you comeout of the block, 
# the resource willbe closed automatically
#We must write thise codes into a func
#if we dont write this into a func, it will execute many times.
# We want it to execute when we call it

#---------------------------------------------------------------------------------#

def createTitle (filename):
    try:
        with open(filename, 'wt')as filehandler:
            # here | (pipe) is used as delimiter
            # we can use delimiter to split the line into multiple data
            # Televisyen|20|1455.55 
            filehandler.write("Product|Quantity|Price")
    except Exception as e:
        print("Something went wrong when we create the header: ", e)
#---------------------------------------------------------------#

def addProduct(filename):
    try:
        product = keyboardInput(str, "Product: ", "Product must be string")
        quantity = keyboardInput(int, "Quantity: ", "Quantity must be integer")
        price = keyboardInput(float, "Price: ", "Price must be float")
        with open(filename, "at") as filehandler:
            filehandler.write(f"\n{product}|{quantity}|{price}")

    except Exception as e:
        print("Something went wrong when we add the product: ", e)


#-------------------------------------------------------------------------------#

def printProduct(filename):
    try:
        lines= None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()#this will give us in list

        #strip will remove the last character like \n , - 
        #split will give the value after the split
        for index, line in enumerate(lines):
            product, quantity, price = line.strip().split("|")
           
            if (index==0):
                print(f"{"No.":5}{product:40} {quantity:>20} {price:>20}") #the :40 :20 is for spacing purpose
                print("=" *80)

            else: 
                print(f"{index:<5}{product:40}{int(quantity):>20}{float(price):>20.2f}") #the :40 :20 is for spacing purpose

    except Exception as e: 
        print("Something went wrong when we print the product: ", e)
#---------------------------------------------------------------------------------#

def editProduct(filename):
    try:
        #lines=None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        index = keyboardInput(int, "Please key in index of the product:", "Index must be integer")
        if index >= len(lines):#to access the row of the products
            #if the index is >= len lines,the product is actually not available
            print("Sorry product not available")
        else:
            product, quantity, price = data[index]
            print(f"Product: {product}\nQuantity: {quantity}\nPrice: {price}")
            confirm = keyboardInput(str," Are you sure you want to edit this product (y/n)?","Respond not valid")
            if (confirm=="y"):
                newproduct = keyboardInput(str, f"Product[{product}]: ", "Product must be string", product)
                newquantity = keyboardInput(int, f"Quantity[{quantity}]: ", "Quantity must be integer", quantity)
                newprice = keyboardInput(float, f"Price[{price}]: ", "Price must be float", price)
                data[index] = [newproduct, newquantity, newprice]
                newlines = []
                for product in data:
                    line= "|".join(map(str, product)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open (filename, "wt") as filehandler:
                    filehandler.writelines(newlines)


    except Exception as e:
        print("Something went wrong when we edit the products: ", e)
#----------------------------------------------------------------------------------------#

def deleteProduct(filename):
    try:
        lines=None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        index = keyboardInput(int, "Please key in index of the product:", "Index must be integer")
        if index >= len(lines):#to access the row of the products
            #if the index is >= len lines,the product is actually not available
            print("Sorry product not available")
        else:
            product, quantity, price = data[index]
            print(f"Product: {product}\nQuantity: {quantity}\nPrice: {price}")
            confirm = keyboardInput(str," Are you sure you want to delete this product (y/n)?","Respond not valid")
            if (confirm=="y"):
                del data[index]
                newlines = []
                for product in data:
                    line= "|".join(map(str, product)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open (filename, "wt") as filehandler:
                    filehandler.writelines(newlines)


    except Exception as e:
        print("Something went wrong when we edit the products: ", e)

#--------------------------------------------------------------------------------------#

filename = "fruit.txt"
createFile(filename)
doMenu(filename)
#addProduct(filename)
#printProduct (filename)
