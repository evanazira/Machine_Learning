#LINK TO QUESTIONS == https://colab.research.google.com/drive/110FxaU_xsPmmQESK_kMDxn4wSCed3cBS?usp=sharing&classId=e075e06b-4c4e-4212-9ae4-e506090eaed0&assignmentId=c7370762-3068-4c3b-b26e-7656dca71121&submissionId=4ccafc55-d3b6-5a6d-86bd-834cea0fc81f
#Q1
integer = input("Enter a number: ")
remainder = int(integer) % 2
if (remainder == 1):
  print(f"Your integer {integer} is an odd number")

else:
  print(f"Your integer {integer} is an even number")


#Q2
score = int(input("Enter your score: "))
if(score >= 90 and score <= 100):
  print("You got A")
elif(score >= 80 and score <= 89):
  print ("You got B")
elif(score >= 70 and score <= 79):
  print ("You got C")
elif(score >= 60 and score <= 69):
  print ("You got D")
elif(score >= 0 and score <= 60):
  print ("You got F")
else:
  print("Your score is invalid") #if input score is more that 100 or a negative number

#Q3
year = int(input("Enter the year: "))
checkYear = year % 4
if (checkYear == 0):
  print(f"The year {year} is a leap year")
else:
  print(f"The year {year} is not a leap year")

#Q4
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if(num1 > num2 and num1 > num3):                    #if no 1 is the biggest
  print(f"The largest number entered is {num1}")
elif (num2 > num1 and num2 > num3):                 #if no 2 is the biggest
  print(f"The largest number entered is {num2}")
elif (num3 > num1 and num3 > num2):                 #if no 3 is the biggest
  print(f"The largest number entered is {num3}")
elif (num1==num2 and num1<num3):                    #if no 1 and no 2 is same and no 3 is the biggest
  print(f"The largest number entered is {num3}")
elif (num1==num3 and num1<num2):                    #if no 1 and no 3 is same and no 2 is the biggest
  print(f"The largest number entered is {num2}")
elif (num2==num3 and num2<num1):                    #if no 2 and no 3 is same and no 1 is the biggest
  print(f"The largest number entered is {num1}")
elif (num1==num2 and num1>num3):                    #if no 1 and no 2 is same and no 1 and no 2 are the biggest
  print(f"The largest number entered is {num1}")
elif (num1==num3 and num1>num2):                    #if no 1 and no 3 is same and no 1 and no 3 are the biggest
  print(f"The largest number entered is {num1}")
elif (num2==num3 and num2>num1):                    #if no 2 and no 3 is same and no 2 and no 3 are the biggest
  print(f"The largest number entered is {num2}")
else:                                               #if num1=num2=num3
  print(f"All numbers that you entered are the same value")

#Q5
character = input("What is your alphabet character? ")
if (character=='a' or character=='e' or character=='i' or character=='o' or character=='u'or character=='A' or character=='E' or character=='I' or character=='O' or character=='U'):
  print(f"The character you entered {character} is vowel")
else:
  print(f"The character you entered {character} is consonant")


#Q6
weight = float(input("Your body weight(kg): "))
height = float(input("Your height(m): "))
BMI = weight / (height ** 2)
if (BMI < 18.5 and BMI>=0):
  print(f"Your BMI is {BMI} and you are Underweight")
elif (BMI >= 18.5 and BMI < 24.9):
  print(f"Your BMI is {BMI} and you have a normal weight")
elif (BMI >= 25 and BMI <29.9):
  print(f"Your BMI is {BMI} and you are Overweight")
elif (BMI >= 30):
  print(f"Your BMI is {BMI} and you have an obesity")
else:
  print(f"Invalid weight or height value")

#Q7
side1 = float(input("Enter length of side 1 of the triangle: "))
side2 = float(input("Enter length of side 2 of the triangle: "))
side3 = float(input("Enter length of side 3 of the triangle: "))

if(side1 == side2 and side1 == side3):                     #side1=side2=side3
  print("This triangle is Equilateral")
elif(side1 == side2 or side1 == side3 or side2 == side3):  #when 2 of the sides are the same length
  print("This triangle is Isosceles")
else:
  print("This triangle is Scalene")                        #each side has different length

#Q8
withdrawalAmaount = int(input("How much you want to withdraw? "))
checkBill = withdrawalAmaount % 10
if (checkBill == 0):                            #if the amount is multiply of 10 and remainder is 0
  bill50 = withdrawalAmaount // 50              #the number of bill 50
  bill20 = (withdrawalAmaount %50 )//20         #the number of bill 20
  bill10 = ((withdrawalAmaount %50) %20 )//10   #the number of bill 10
  print(f"RM 50 = {bill50} bill \n RM 20 = {bill20} bill \n RM 10 = {bill10} bill")
else:                                       #if the amount is multiply of 10 but has remainder
  bill50 = withdrawalAmaount // 50              #the number of bill 50
  remainderbill50 = withdrawalAmaount % 50
  bill20 = remainderbill50 // 20                #the number of bill 20
  bill10 = ((remainderbill50) % 20) // 10       #the number of bill 10
  bill1 = remainderbill50 % 10                  #the number of bill 1
  print(f"RM 50 = {bill50} bill \n RM 20 = {bill20} bill \n RM 10 = {bill10} bill \n RM 1 = {bill1} bill")
  print("There is no 1 dollar bill that can be withdraw")


#Q9 (betulkan guna input user)
number = int(input("Enter a whole number from 100 until 999: "))
givenNum = number #only for printing the input number

if (number>=100 and number<1000):
  print("The number entered: ", number)
  #square of original number
  numSquared = number ** 2
  OrinumSquared = numSquared #only for printing the value of numSquared
  print("The squared of the number: ", numSquared)
 
  #reverse of square of original number
  revOrinumSquared=0
  if (OrinumSquared>=10000 and OrinumSquared<=99999): #if the squared number have 5 digit
    revOrinumSquared = revOrinumSquared*10 + (numSquared % 10)
    numSquared //= 10         
    revOrinumSquared = revOrinumSquared*10 + (numSquared % 10)
    numSquared //= 10         
    revOrinumSquared = revOrinumSquared*10 + (numSquared % 10)
    numSquared //= 10         
    revOrinumSquared = revOrinumSquared*10 + (numSquared % 10)
    numSquared //= 10         
    revOrinumSquared = revOrinumSquared*10 + (numSquared % 10)
    
  else:                                                     #if the squared number have 6 digit  
    revOrinumSquared = revOrinumSquared*10 + (numSquared % 10)
    numSquared //= 10         
    revOrinumSquared = revOrinumSquared*10 + (numSquared % 10)
    numSquared //= 10         
    revOrinumSquared = revOrinumSquared*10 + (numSquared % 10)
    numSquared //= 10         
    revOrinumSquared = revOrinumSquared*10 + (numSquared % 10)
    numSquared //= 10         
    revOrinumSquared = revOrinumSquared*10 + (numSquared % 10)
    numSquared //= 10         
    revOrinumSquared = revOrinumSquared*10 + (numSquared % 10)
  
  print("The value of the reverse of the Squared number: ", revOrinumSquared) 
    
    
  #reverse of number
  revnum=0
  revnum = revnum*10 + (number % 10)
  number //= 10         
  revnum = revnum*10 + (number % 10)
  number //= 10         
  revnum = revnum*10 + (number % 10)
  print("The value of the reversed number: ",revnum)


  # square of reverse number
  revnumSquared = revnum ** 2
  print("The value of squared of reversed number: ",revnumSquared)


  if(revnumSquared == revOrinumSquared):
    print(f"The given number is {givenNum}. Its reversed number is {revnum}. The squared of these numbers are {OrinumSquared} and {revnumSquared}. ")
    print(f"The number {givenNum} is an Adam Number.")
    
  else:
    print(f"The given number is {givenNum}. Its reversed number is {revnum}. The squared of these numbers are {OrinumSquared} and {revnumSquared}. ")
    print(f"The number {givenNum} is not an Adam Number.")

else:
   print(f"The number {givenNum} you entered is not between 100 untill 999!")



#Q10 (betulkan tak yah guna input user)
number = int(input("Enter a number between 0 to 9999: "))
if(number >= 0 and number < 10):
  #the input number is 1 digit
  #the number will be to the power of 1
  result = number ** 1
  print(f"The sum of {number}^1 is", result)

  if (number == result):                                     #to compare the input number and its result value
    print(f"The number {number} is an Armstrong number")

  else:
    print(f"The number {number} is not Armstrong number")

elif (number >= 10 and number < 100):
  #it means the input number is 2 digit
  #split the 2 digit
  #each digit will be to the power of 2
  a0 = number // 10 #-->to get 1st digit
  a1 = number % 10 #-->to get 2nd digit
  result = (a0 ** 2) + (a1 ** 2)
  print(f"The sum of {a0}^2 + {a1}^2  is", result)

  if (number == result):
    print(f"The number {number} is an Armstrong number")

  else:
    print(f"The number {number} is not Armstrong number")

elif (number >= 100 and number < 1000 ):
  #it means the input number is 3 digit
  #split the 3 digit
  #each digit will be to the power of 3
  b0 = number // 100 #-->to get 1st digit
  b1 = (number % 100) // 10 #-->to get 2nd digit
  b2 = (number % 100) % 10 #-->to get 3rd digit
  result = (b0 ** 3) + (b1 ** 3) + (b2 ** 3)
  print(f"The sum of {b0}^3 + {b1}^3 + {b2}^3 is", result)

  if (number == result):
    print(f"The number {number} is an Armstrong number")

  else:
    print(f"The number {number} is not Armstrong number")

elif (number >= 1000 and number < 10000 ):
  #it means the input number is 4 digit
  #split the 4 digit
  #each digit will be to the power of 4
  b0 = number // 1000 #-->to get 1st digit
  b1 = (number % 1000) // 100 #-->to get 2nd digit
  b2 = ((number % 1000) % 100) // 10 #-->to get 3rd digit
  b3 = ((number % 1000) % 100) % 10 #-->to get 4th digit
  result = (b0 ** 4) + (b1 ** 4) + (b2 ** 4) + (b3 ** 4)
  print(f"The sum of {b0}^4 + {b1}^4 + {b2}^4 + {b3}^4 is", result)

  if (number == result):
    print(f"The number {number} is an Armstrong number")

  else:
    print(f"The number {number} is not Armstrong number")

else:
  print("The input number is not between 0 to 9999")
