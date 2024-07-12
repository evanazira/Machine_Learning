#when ever u want to iterate a list of items then you must use for loop
fruits = ["appel","rambutan","orange","durian","mango","cempedak","banana","mangosteen","grape"]
#          -9         -8        -7       -6      -5        -4        -3        -2         -1
#print all items in the list
for fruit in fruits: #fruit is a temporary variable. to hold current items until the block of code is executed fully
    print(fruit)

#print all item in the even position
for fruit in fruits[::2]:
    print(fruit)

#print only fruit with 6 letter
for fruit in fruits:
    if(len(fruit)==6):
        print(fruit)

#we want to know each fruit together with the index (position)
position = 0
for fruit in fruits:
    print(position, fruit)
    position += 1

#I want to create a multipliction table of 5
# 1 x 5 = 5
# 2 x 5 = 10
multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
multiplicant = 5
for multiplier in multipliers:
    print(multiplier, "x", multiplicant, "=", multiplier *multiplicant)


#however this is not practical when list is until 200 instead of 12
#we have to go for range option start_index:end_index
#but the : operator only on an array
#

print(list(range(1,13)))

multiplicant = 6
for multiplier in range(1,13):
    print(multiplier, "x", multiplicant, "=", multiplier *multiplicant)


#givennumber = input("Give me a number: ")
givennumber = 97409
while(givennumber > 0):
    print(givennumber % 10**5)
    givennumber //= 10



number = 12345
numberofdigit = len(str(number))-1
while (number>0):
    print(number//10**numberofdigit)
    number %= 10**numberofdigit
    numberofdigit-= 1
#split numbers without 
number = 12345
numberofdigit = len(str(number))
while (number>0):
    print(number//10**numberofdigit)
    number %= 10**numberofdigit
    numberofdigit-= 1

number = 12345
strnumber = str(number) #list of character
for digit in strnumber:
    print(digit)

#to print the individual digit in reverse
number = 12345
strnumber = str(number) #list of character
for digit in strnumber[::-1]:
    print(digit)


fruits = ["apple", "orange","banana", "mango" ,"grapes"]

for fruit in fruits:
    print(fruit)
    if  (fruit =="mango"): break


multiplicant = 6
multiplier = 1
while (multiplier <=12):
    print(multiplier, "x" , multiplicant, ("= "), multiplicant*multiplier)
    multiplier += 1
    if multiplier == 11: break

else:
    print("Multiplacation table done")


multiplicant = 10
multiplier = range(1,13)
for multipliers in multiplier:
    if multipliers %5 == 0: continue #the 5 X 10 = 50 and 10 X 10 = 100 are skip
    print(multipliers, "x" , multiplicant, ("= "), multiplicant*multipliers)
    #multiplier += 1
    