first_name = "Eva Nazira"
last_name = "Nazry Syah" 
#addition is an operator that used numbers only
#for strings it is called 'string concatenation'
full_name = first_name + " " + last_name
print(full_name)

carPlate = "UTM"
Number = 381
#however this usse case cannot add them because one is number and  another is string
#carPlateNumber = carPlate + Number
#convert number to string using str function
carPlateNumber = carPlate + str(Number)
print (carPlateNumber)

#in python you can multiple string with integer
#when we do this it will produce 'times' effect
product = 'book'
print(product * 5)
print('=' * 40)

#we can use triple double quote aor triple single quote to create multiline string
#\n is for next line
#\t is fot tab
#\r is for carriage return 
message=  "As I am not feeling well.\n "
message = message + "I wont be able to attend the meeting\n"
message += "Please proceed...\n"
print(message)

message=  '''As I am not feeling well. 
I won't be able to attend the meeting 
Please proceed...'''
print(message)

myfile="c:\newfolder\table\read.txt"
print (myfile)
#c:\newfolder\table\read.txt  the \n \t and \r will beexecuted by python...to avoid this we 
#need to tell python to ignore escape sequence
#need to add \\
myfile="c:\\newfolder\\table\\read.txt"
print (myfile)
#we also have special string called raw string
myfile=r"c:\newfolder\table\read.txt"
print (myfile)


#relationship btw string and list
#strings are noting but list of character
mygreeting = "Hello world"
print(mygreeting[0])
print(mygreeting[0:6])
print(mygreeting[::2])
print(mygreeting[::-1])
#how many character we have in mygreeting
print(len(mygreeting))


#reverse the givennumber
givennumber = 97531
strgivennumber = str(givennumber)
print(int((strgivennumber[::-1])))

#when i started this python class I said all these literals are objects
#"Televisyen" is a string literal/ string value
#televisyen ias also called string object
#object have func inside


#argv = ["abc","def"]
product = "Televisyen"
print(product.split()) #this split func takes the litera; assigne to the variable and split them (tokanize them) inro multiple words (seperated by space)
#since it is hoing to return more than 1 word it is goinf to be list of words
#function inside the object is also called "method"
