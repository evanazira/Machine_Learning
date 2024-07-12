#find the perfect factors of a number
'''
num = 1
count = 0

while count<4:
    proper_divisor = []
    sum = 0

    for i in range(1,num):
        if num % i == 0:
            proper_divisor.append(i)
    #print(proper_divisor)

    #find the sum of the perfect factors
    for factor in proper_divisor:
        sum = sum + factor
    #print(sum)
    
    if sum==num:
        print(f"The number {num} is a perfect number. Its perfect factor are {proper_divisor}")
        count += 1

    num += 1
    


num=1
count = 0
while count<4:
    primetest = (2**num) - 1

#N = int(input(""))
count = 0
num=2 #testlist for primenum

while(count < 4):
    isPrime = True
    
    for i in range(2,num):
     if (num %i==0):
       isPrime = False
       break
    
    if (isPrime==True):
        if((2**num) - 1)==num:
            print(num,end=" ")
            count += 1
    num += 1a=(1,2,3)
b=('A','B','C')
c=zip(a,b)      #returns Zip Object
print(list(c))'''
'''
def writer():
title = 'Sir'
name = (lambda x:title + ' ' + x)
return name   
who = writer()
print(who('Arthur'))
a=(1,2,3)
b=('A','B','C')
c=zip(a,b)
print (c)
''''''
name = input("Enter the name: ")
n = int(input("Enter the position (1-based) of the word to remove: "))

# Split the name into words
name_list = name.split("")

# Check if the nth word exists in the list
if 1 <= n <= len(name_list):
    # Delete the nth word (adjusting for 1-based input)
    del name_list[n - 1]
    print(name_list)
else:
    print("Invalid position. Please enter a valid position within the range.")

''''''

num1 = int(input())
num2 = int(input())

if(a<2):
     a=2
prime = []

for num in range(a,b + 1):
    for i in range(2,num):
#numbers = range(a,b)
#divisors = range(a,b)

        if(num % i== 0):
            break
       

    else:
        prime.append(num)
for i in prime:
    print(i, end = " ")

num1 = int(input())
num2 = int(input())
if num1 > num2:
     a = num2
     b = num1

else:
    a = num1
    b = num2
prime = []

for num in range(a,b + 1):
    for i in range(2,num):
#numbers = range(a,b)
#divisors = range(a,b)

        if(num % i== 0):
            break
    else:
        prime.append(num)
for i in prime:
    print(i, end = " ")
'''
def open_text_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Contents of {filename}:")
            print(content)
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"Error: {e}")

def doMenu():
    while True:
        print("Menu:")
        print("1. Open file1.txt")
        print("2. Open file2.txt")
        print("3. Open file3.txt")
        print("Q. Quit")
        
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == '1':
            open_text_file("file1.txt")
        elif choice == '2':
            open_text_file("file2.txt")
        elif choice == '3':
            open_text_file("file3.txt")
        elif choice == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or Q.")

# Example usage
doMenu()