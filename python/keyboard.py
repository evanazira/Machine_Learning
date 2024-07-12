#pyhton have build in function called input
#the input function takes the single parameter (caption/ question)
#input function will display the caption and wait for the user input
#the input is always of type string

firstnumber = input ("Enter 1st number ")
print (firstnumber)
print (type(firstnumber))


secondnumber = input("Enter 2nd Number: ")
print (firstnumber + secondnumber) # string concatenation
print(int(firstnumber) + int(secondnumber))  #addition

number = input("Enter the numbers to do total:")
numberlist = number.split(",") #if we do not put the(",") it will split by space
print(numberlist)
total = 0
for number in numberlist:
    #int func trim the string value remove the spaces in the string and then convert string into integer
    total = total + int(number)
print (total)