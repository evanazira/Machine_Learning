#Q1
#Prompts the user to enter two numbers. Stores these numbers in two variables. 
#Performs and prints the results of addition, subtraction, multiplication, and division of these two numbers.
firstnum = input("Enter first number: ")
secondnum = input("Enter second number: ")
addition = (float (firstnum) + float(secondnum))
subtraction = (float (firstnum) - float(secondnum))
multiplication = (float (firstnum) * float(secondnum))
division = (float (firstnum) / float(secondnum))
print("Addition =  ", addition )
print("Subtraction =  ", subtraction)
print("Multiplication =  ", multiplication)
print("Division =  ", division)

#Q2
#Prompts the user to enter a temperature in Celsius. Converts the temperature to Fahrenheit. 
#Prints the temperature in Fahrenheit. (Hint: The formula to convert Celsius to Fahrenheit is: F = C * 9/5 + 32)
temp = float(input("What is today's temperature in Celsius? "))
Fahrenheit = temp * (9/5) + 32
print(f"Today's is {Fahrenheit} F")

#Q3
#Prompts the user to enter the length and width of a rectangle. 
#Calculates the area and perimeter of the rectangle. Prints the area and perimeter.
length = float(input("What is the length of the rectangle? "))
width = float(input("Whaat is the width of the rectangle? "))
area = length * width
perimeter = 2* (length + width)
print(f"Area of rectangle : {area}")
print(f"Perimeter of rectangle : {perimeter}")

#Q4
#Prompts the user to enter the principal amount, rate of interest, and time in years. 
#Calculates the simple interest. 
#Prints the simple interest. 
#(Hint: The formula to calculate simple interest is: SI = (P * R * T) / 100)
principal = input("Enter the principal amount: ")
interestRate = input("Enter the rate of interest: ")
time = input("Enter time in years: ")
simpleInterest = (float(principal) * float(interestRate) * float(time))/100
print("Your Simple Interest is: ", simpleInterest)

#Q5
#Prompts the user to enter two numbers. Swaps the values of the two variables. 
#Prints the values before and after swapping.
firstnum = input("Enter the 1st number: ")
secondnum = input("Enter the 2nd number: ")

firstnumSwab = secondnum
secondnumSwab = firstnum

print(f"First Number and Second Number before swab are {firstnum} and {secondnum}")
print(f"First Number and Second Number after swab are {firstnumSwab} and {secondnumSwab}")


#Q6
#Prompts the user to enter a number. Calculates the square and cube of the number. 
#Prints the square and cube.
number = input ("Enter a number: ")
numSquared = int(number)** 2
numCubed = int(number) **3
print("The value of the number when squared and cubed are", numSquared, "and" , numCubed)

#Q7
#Prompts the user to enter their weight in kilograms and height in meters. 
#Calculates the Body Mass Index (BMI). Prints the BMI. 
#(Hint: The formula to calculate BMI is: BMI = weight / (height * height))
weight = input("Your body weight(kg): ")
height = input("Your height(m): ")
BMI = (float(weight) / (float(height) * float(height)))
print(f"Your BMI is {BMI}")

#Q8
#Prompts the user to enter the principal amount, rate of interest, time in years, 
#and number of times interest is compounded per year. 
#Calculates the compound interest. Prints the compound interest.

#(Hint: The formula to calculate compound interest is: 
#A=P(1+R/100n)nt where A is the amount, P is the principal amount, R is the annual interest rate,
# t is the time the money is invested for, and n is the number of times interest is compounded per year)
principal = int(input("Enter the principal amount: ")) 
interestRate = int(input("Enter the interest rate: "))
time = int(input("Enter the time in in years: "))
numberofTimes = int(input("Enter the number of times interest is compounded per year: "))
compoundedInterest = principal * ((1 + interestRate) / (100 * numberofTimes)) * numberofTimes * time
print("The compound interest is", compoundedInterest)

#Q9
#Converts the given integer 97409 to its binary representation. Prints the binary representation.
N = 97409
a0 = N % 2 # to find the remaider
b0 = N // 2 #to find the quotient
a1 = b0 % 2
b1 = b0 // 2
a2 = b1 % 2
b2 = b1 // 2
a3 = b2 % 2
b3 = b2 // 2
a4 = b3 % 2
b4 = b3 // 2
a5 = b4 % 2
b5 = b4 // 2
a6 = b5 % 2
b6 = b5 // 2
a7 = b6 % 2
b7 = b6 // 2
a8 = b7 % 2
b8 = b7 // 2
a9 = b8 % 2
b9 = b8 // 2
a10 = b9 % 2
b10 = b9 // 2
a11 = b10 % 2
b11 = b10 // 2
a12 = b11 % 2
b12 = b11 // 2
a13 = b12 % 2
b13 = b12 // 2
a14 = b13 % 2
b14 = b13 // 2
a15 = b14 % 2
b15 = b14 // 2
a16 = b15 % 2
b16 = b15 // 2

#result = str (a16) + str(a15) + str(a14) + str (a13) + str(a12) + str(a11) + str (a10) + str(a9) + str(a8) + str (a7) + str(a6) + str(a5) + str(a4)

print (f"The binary for integer {N} is {a16} {a15} {a14} {a13} {a12} {a11} {a10} {a9} {a8} {a7} {a6} {a5} {a4} {a3} {a2} {a1} {a0}")


#Q10
#Converts the given binary 1011 to its decimal representation. Prints the decimal representation.
binarynum = 1011
a0 = (binarynum // 1000) * 2**3
a1 = ((binarynum // 100) % 10) * 2**2
a2 = (binarynum % 10) * 2**1
a3 = (binarynum % 10) * 2**0
decimalnum = a0 + a1 + a2 + a3
print("The decimal representation for binary 1011 is",decimalnum)