#Q1
naturalNum = 1
while (naturalNum <= 10):
    print(naturalNum)
    naturalNum = naturalNum + 1

####################################################################################################
#Q2
#no known prime number
count = 10
givenNumber = range(2,51) #testlist for primenum
for givenNumbers in givenNumber:
  isPrime = True
  divisor = range(2, givenNumbers)  #testlist for divisor
  for divisors in divisor: #this repeat for the number in range (2,50) to be divide by the numbers in range (2,50)
    if (givenNumbers %divisors==0):
      isPrime = False
      break

  if (isPrime==True):
    print(givenNumbers) 
    count -= 1
    if (count==0): break


####################################################################################################
#Q2 (alternative)
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

#####################################################################################
#Q3
#input: user will give the number of items of ADAM numbers that they want to generate
#processing: differenciate the natural number and adam number
#output: generate number of items's list of Adam number

#user input
item = int(input("Enter amount of Adam number you want to generate: "))
count = 0
num = 0
adam_number=[] #empty list of Adam number

while(count<item):
    #check if num is Adam number
    testNum = num
    revtestNum_str = str(testNum)
    revtestNum = int(revtestNum_str[::-1])
    testNum_sqr = testNum**2
    revtestNum_sqr = revtestNum**2
    revtestNum_sqr_str = str(revtestNum_sqr)
    inv_revtestNum_sqr = int(revtestNum_sqr_str[::-1])

    #to check if the testNum**2 == inverse_revtestNum**2
    if (testNum_sqr == inv_revtestNum_sqr):

        #make the num in list type so that it can be added into the adam_number list
        adam_number = adam_number + [num]
        #adam_number.append (num) #altenative to add Adam number in the list
        count += 1
        num+=1

    else:
        num += 1

print (f"The first {item} Adam numbers are:",adam_number)

#######################################################################################
#Q4
item = int(input("Enter the amount of Armstrong Number you want to generate: "))
num = 0
count = 0
armstrong_num = []

while(count<item):
    num_str = str(num)
    num_digit = len(num_str)
    sum_of_power = 0

    for digit in num_str:
        sum_of_power += int(digit)**num_digit

    if(sum_of_power==num):
        count +=1
        armstrong_num += [num]
        num +=1

    else:
        num +=1

print (f"The first {item} Armstrong numbers are:",armstrong_num)

###########################################################################################
#Q5
pattern = "o"
count = 0
while(count<5):
  print(pattern)
  pattern += "o"
  count +=1

#########################################################################################
#Q6
for row in range(1,6):   #repeat for row
  print ("row ",row)
  for column in range(1, row + 1):  #repeat for column
    print(column, end=" ")

  print(" ")

  ####OUTPUT####
  '''
    row  1
    1  
    row  2
    1 2  
    row  3
    1 2 3  
    row  4
    1 2 3 4  
    row  5
    1 2 3 4 5  
  '''