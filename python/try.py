'''
givenNumber = range(2,51)
count = 10
for givenNumbers in givenNumber:
    if(count>0 and count<=10):
        isPrime = True
        divisors = range(2,givenNumbers)
        for divisor in divisors:
            if (givenNumbers % divisor==0):
                isPrime =False
                break
        
        if (isPrime==True):
            print(givenNumbers)
            count -= 1

    else:
        break
'''''''
people_show1 = int(input("Enter the number of people who watched show 1\n"))
avg_rate_show1 = float(input("Enter the average rating for show 1\n"))
people_show2 = int(input("Enter the number of people who watched show 2\n"))
avg_rate_show2 = float(input("Enter the average rating for show 2\n"))
people_show3 = int(input("Enter the number of people who watched show 3\n"))
avg_rate_show3 = float(input("Enter the average rating for show 3\n"))

total_rate_show1 = people_show1 * avg_rate_show1 
total_rate_show2 = people_show2 * avg_rate_show2 
total_rate_show3 = people_show3 * avg_rate_show3 
overall_avg_rate = (total_rate_show1 + total_rate_show2 + total_rate_show3) / (people_show1 + people_show2 + people_show3)

print("The overall average rating for the show is ",overall_avg_rate)

string = input("Enter numbers seperated by commas: ")
num_strings = string.split(",")
numbers = []
for num_int in num_strings:
  num = int(num_int.strip()) #to remove any space between the commas and number
  numbers = numbers + [num]

new_list = []
print(numbers)
for digit in numbers:
    if (digit not in new_list):
        print("all numbers are unique")
        #to find the 3 uniques numbers that the sum of it is 100
    for i in range (len(numbers)):
        for j in range (i + 1, len(numbers)):
            for k in range (j + 1, len(numbers)):
                num1 = numbers[i]
                num2 = numbers[j]
                num3 = numbers[k]

        sum=False
        #if the sum numbers is 100, then it is True
        if (num1+num2+num3==100):
          print(f"The sum of number {num1},{num2} and {num3} is 100")
          sum=True
          break

        if sum:
         break
    if sum:
      break

  if not sum:
    print("No combination of numbers entered equals to 100")


else:
  print("Not all numbers are unique")


size = (input(""))
element = input("")
elements = element.split(" ")

 
for i in elements:
    count = 0
    for j in elements:
        if (i==j):
            count += 1
        if(i==1):
            print(i,end="")

h = int(input(""))
count = 0
num=2 #testlist for primenum

while(count < h):
    isPrime = True
    for i in range(2,num):
     if (num %i==0):
       isPrime = False
       break
     
     if (isPrime==True):
        print(num,end="")
        count += 1
    num += 1
''''''''
string=input("Give me a string of numbers seperated by comma: ")
stringsplit = string.split(",")
inputNum = []

for num_str in stringsplit:
    inputNum.append(int(num_str))

#check all number
all_unique = True
for i in range(len(inputNum)):
    for j in range(i+1, len(inputNum)):
        if inputNum[i] == inputNum[j]:
            all_unique = False
            break

if all_unique==True:
    print("All numbers are different")

else:
    print("Not all numbers are different")
''''''
uniqueNum = []

for num in inputNum:
    if num not in uniqueNum:
        uniqueNum.append(num)
print("the uniq num in input num is ", uniqueNum)

''''''
for i in range(len(uniqueNum)):
    for j in range(i+1,len(uniqueNum)):
        for k in range(j+1,len(uniqueNum)):
            if uniqueNum[i] +uniqueNum[j] + uniqueNum[k]==100:
                print(uniqueNum[i],uniqueNum[j],uniqueNum[k])
                break

string=input("Give me a string of numbers seperated by comma: ")
stringsplit = string.split(",")
inputNum = []

for num_str in stringsplit:
    inputNum.append(int(num_str))

#check all number
all_unique = True
for i in range(len(inputNum)):
    for j in range(i+1, len(inputNum)):
        if inputNum[i] == inputNum[j]:
            all_unique = False
            break

if all_unique==True:
    print("all numbers are unique")
  #to find the 3 uniques numbers that the sum of it is 100
    for i in range (len(inputNum)):
        for j in range (i + 1, len(inputNum)):
            for k in range (j + 1, len(inputNum)):
                num1 = inputNum[i]
                num2 = inputNum[j]
                num3 = inputNum[k]

                sum=False
                #if the sum numbers is 100, then it is True
                if (num1+num2+num3==100):
                    print(f"The sum of number {num1},{num2} and {num3} is 100")
                    sum=True
                    break

            if sum==True:
                break
        if sum:
            break

    if not sum:
        print("No combination of numbers entered equals to 100")

else:
    print("Not all numbers are different")
    ''''''
for i in range(1,101):
    if (i%3==0 and i%5==0):
        print ("FizzBuzz")

    if (i%3==0):
        print ("Fizz")

    if (i%5==0):
        print("Buzz")
    
    else:
        print(i)
N = int(input(""))
count = 0
num=2 #testlist for primenum

while(count < N):
    isPrime = True
    for i in range(2,num):
     if (num %i==0):
       isPrime = False
       break
     
    if (isPrime==True):
        print(num,end=" ")
        count += 1
    num += 1



N = int(input("Enter"))
FN = 30
SN = 35
count1 = 0
count2 = 0
count3 = 0
sequenceList = []
while count1<N:
    if(count1 % 2 == 0):#even
        FN += count2
        count2 += 8
        sequenceList = sequenceList + [str(FN)]

    elif(count1 % 2 != 0): #odd
        SN += count3
        count3 += 6
        sequenceList = sequenceList + [str(SN)]
    count1 += 1

for i in sequenceList:
    print(i, end = " ")


variable = (input("A B N: "))
variable = variable.split(" ")
turn = 0
C = int(variable[0])
D = int(variable[1])
N = variable[2]
score = 0

while turn < int(N):
    
    if (turn%2==0):
        C = C * 2
        
    elif (turn%2!=0):
        D = D* 2

    
    turn += 1
score = C + D
print(score)



print({'b', 'a', 'r'} & set('qux'))

n=4
count = 0
num = 0
while count<n:
    check = (2**num) * ((2**num) - 1)

    num += 1
    count+=1





def sum_of_proper_divisors(n):
    """ Function to calculate the sum of proper divisors of n """
    if n <= 1:
        return 0
    
    sum_divisors = 1  # Start with 1 because 1 is a proper divisor for all n > 1
    sqrt_n = int(n**0.5)
    
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
                
    return sum_divisors

def find_perfect_numbers(count):
    """ Function to find the specified number of perfect numbers """
    perfect_numbers = []
    num = 2  # Starting from 2, as 1 is not a perfect number
    
    while len(perfect_numbers) < count:
        if sum_of_proper_divisors(num) == num:
            perfect_numbers.append(num)
        num += 1
    
    return perfect_numbers

# Find the first 4 perfect numbers
perfect_numbers = find_perfect_numbers(4)

# Print the perfect numbers and their divisors
for num in perfect_numbers:
    divisors = [i for i in range(1, num) if num % i == 0]
    print(f"{num}: The divisors of {num} are {divisors} and the sum of proper divisors is {sum(divisors)}.")
'''
#num=1
#count = 0
#while count<4:
  #  primetest = (2**num) - 1

'''
count = 0
num=2 #testlist for primenum

while(count< 4):
    #check if it is prime number
    isPrime = True
    for i in range(2,num):
     if (num %i==0):
       isPrime = False
       break
    
    if (isPrime==True):
            mersenne_prime = (2**num) - 1
            mersenne_prime_is_prime = True
            for j in range(2, int(mersenne_prime**0.5)+1):
                if mersenne_prime%j == 0:
                    mersenne_prime_is_prime = False
                    break
            if mersenne_prime_is_prime:
                perfect_num = (2**(num-1)) * mersenne_prime

                #print(num,end=" \n")
            
                count += 1
            print(f"Perfect Number {count}:", perfect_num)
    
    num += 1


def convert_to_words(num):  
    if num == 0:  
        return "zero"  
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]  
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]  
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]  
    words = ""  
    if num>= 1000:  
        words += ones[num // 1000] + " thousand "  
        num %= 1000  
    if num>= 100:  
        words += ones[num // 100] + " hundred "  
        num %= 100  
    if num>= 10 and num<= 19:  
        words += teens[num - 10] + " "  
        num = 0  
    elif (num>= 20):  
        words += tens[num // 10] + " "  
        num %= 10  
    if num>= 1 and num<= 9:  
        words += ones[num] + " "  
    return words.strip()  
num = int(input("Enter a number"))  
words = convert_to_words(num)  
print(words)   '''
# Python program to convert Roman Numerals
# to Numbers

# This function returns value of each Roman symbol
'''

def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1


def romanToDecimal(str):
    res = 0
    i = 0

    while (i < len(str)):

        # Getting value of symbol s[i]
        s1 = value(str[i])

        if (i + 1 < len(str)):

            # Getting value of symbol s[i + 1]
            s2 = value(str[i + 1])

            # Comparing both values
            if (s1 >= s2):

                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s1
                i = i + 1
            else:

                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1

    return res


# Driver code
print("Integer form of Roman Numeral is"),
print(romanToDecimal("MCMIV"))

def intToRoman(num):
    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    
    return (thousands[num // 1000] +
            hundreds[(num % 1000) // 100] +
            tens[(num % 100) // 10] +
            units[num % 10])

# Example usage:
print(intToRoman(3549)) 


'''

'''


def compression(string): 
    hash = {}
    list = []
    count = 0
    for i in range(len(string) - 1): 
        if string[i - 1] != string[i] or i == 0: 
            if string[i] != string[i + 1] or i == len(string) - 2: 
                count = count + 1
                list.append(str(string[i]))
                list.append(str(count))
                count = 0
            elif string[i] == string[i + 1]: 
                count = count + 1
        elif string[i - 1] == string[i]:
            if string[i] != string[i + 1] or i == len(string) - 2: 
                count = count + 1
                list.append(str(string[i]))
                list.append(str(count))
                count = 0
            if string[i] == string[i + 1]: 
                count = count + 1
        #print(list)
    result =  "".join(list)
    for item in list:
        result += item
    if len(result) == len(string): 
        return string
    else: 
        return result
string = input("Enter: ")
print(compression(string))
''''''
num1 = input("").strip()
num2 = input("").strip()

set1 = set(map(int,num1.split(",")))
set2 = set(map(int,num2.split(",")))

symmetrric_diff =sorted(set1.symmetric_difference(set2))

if set1 == set2:
    print ("invalid set")
    
    
else:
    print(set(symmetrric_diff))'''

"""
n = int(input("").strip())
n_str =str(n)

if(len(n_str)<2):
    print("Invalid Input")

firstdigit = int(n_str[0])
lastdigit =  int(n_str[-1])
team = abs(firstdigit - lastdigit)
    
if(team==0):3

    print ("10")

else:
    print(team)"""
# x = ("AEA CAR RENTAL SERVICE SDN BHD")
# c = len(x)
# print(c)

# numSchool= int(input("Enter num school:"))
# count=0
# totalstudent = 0
# for school in range(0,numSchool):
#     numStudent=int(input(f"Enter num student for school{school+1}:"))
#     totalstudent += numStudent

# price = float(input("Price of book:"))
# totalcost = price * totalstudent
# print(f"Total number of books required : {totalstudent}")
# print(totalstudent , totalcost)


# sheets = int(input("Enter total Number of sheets:\n"))
# attendence = []
# for sheet in range(sheets):
#     regNum =tuple(map(int, input().strip().split()))
#     attendence.append(regNum)

# print(f"Attendence Sheets with Register Number: {tuple(attendence)}")

# remDup = set()
# for sheet in attendence:
#     remDup += sheet

# final_sheet = tuple(sorted(remDup))
# print(f"Final sheet: {final_sheet}")

#n = number of students


# n = int(input().strip())

# studentMarks = {}

# for student in range(n):
#     name, mark1, mark2, mark3, mark4 = input("Name,Marks:\n").strip().split(" ")
#     marks = int([mark1,mark2,mark3,mark4])
#     if name not in studentMarks:
#         studentMarks[name] = []
#     studentMarks[name].append(marks)

# desiredStudent = input("Target").strip()

# if desiredStudent not in studentMarks:
#     print("Student doesn't exist")

# else:
#     marks = studentMarks[desiredStudent]
#     #to get the highest marks, must sort and check is the marks are not same
#     uniqueMarks = sorted(set(marks),revrse = True)
#     if len(uniqueMarks)<2:
#         print("All marks are the same")
#     else:
#         print(uniqueMarks[1])

# def greet(name,message = "Welcome to Python Programming"):
#     geeting = print(f"Hello {name}, {message}")

# choose = int(input("Menu\n1.Name and Message\n2. Name"))
# if choose ==1:
#     name = input("Enter the name\n")
#     message = input("Enter the message\n")
#     greet(name,message)

# elif choose==2:
#     name = input("Enter the name\n")
#     greet(name)

# def addition(n1,n2):
#     add = print(f"{n1} + {n2} = {n1+n2}")
#     return add
# def subtraction(n1,n2):
#     sub = print(f"{n1} - {n2} = {n1-n2}")
#     return sub
# def multiplication(n1,n2):
#     mul = print(f"{n1} * {n2} = {n1*n2}")
#     return mul
# def division(n1,n2):
#     div = print(f"{n1} / {n2} = {n1/n2}")
#     return div
# def modulus(n1,n2):
#     mod = print(f"{n1} // {n2} = {n1//n2}")
#     return mod

# print("""
# Select the operation
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# 5.Modulus""")
# choice = int(input("Enter the choice(1/2/3/4/5):\n"))
# n1 = int(input("Enter the first number\n"))
# n2 = int(input("Enter the second number\n"))
# if choice == 1:
#     addition(n1,n2)

# elif choice == 2:
#     subtraction(n1,n2)

# elif choice == 3:
#     multiplication(n1,n2)

# elif choice==4:
#     division(n1,n2)

# elif choice==5:
#     modulus(n1,n2)

# else:
#     print("Invalid Input")


n = int(input("Enter size of list\n"))
elements = []
print("Enter the elements in list")
for element in range(n):
    num = int(input())
    if num%13==0:
        elements.append(num)
print(elements)
# fill your code here

