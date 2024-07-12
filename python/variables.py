#product, quantity, price and available are variables
#the variables in python does not hold the values. It holds the address to the values
product = "Television"             # string
quantity = 2                       # integer
price = 1455.25                    # float
available = True                   # Boolean Value or Literal (True/False)
print ("Product:", product)
print ("Quantity:", quantity)
print ("Price:", price)
print ("Available:", available)

#type is another built in function that tell 4us what is the data type of the variables
print (type(product))
print (type(quantity))
print (type(price))
print (type(available))

Total = quantity * price
print ("Total:",Total)

#IRL uses cases the 10 will not be hard coded
#the 10 is coming from an input device (keyboard)---user key in
#so the input value can be a string which needs to be converted
quantity = "22"
print(type(quantity))
#print(quantity*price)

#type casting is to convert one data type to another
#to convert string to int we have a built in function int
#converrt the string to float we have a built in function float
Total = int (quantity) * float(price)
print(Total)


x=100
# now i want to know the address location where 100 is
#we can use built in function called id
print (id(x))


#however in python, the object 100 is not created first
#the python will scan first and if the object 100 is already exist  
#Then the python will reuse the object instead of re-creating the object
y=100
print(id(y))