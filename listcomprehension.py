#deep copy
fruits = ["apple","orange", "mango","banana", "grapes"]
prices = [1.60,1.20,2.20,4.80,6.20]

overseafruit = []
for fruit in fruits:
    overseafruit.append(fruit)

#using list comprehension    
overseafruit = [fruit for fruit in fruits]


for fruit in fruits:
    print(fruit)
################################################################
pricewithsst=[]
for price in prices:
    price_with_sst = price+(price*6)
    pricewithsst.append(price_with_sst)
print(f"for loop list price with sst{pricewithsst}" )

#using list comprehension
pricewithsst = [price + (price*0.06) for price in prices]
print(f"list comprehension price with sst {pricewithsst}")

#task which we need to do is find pricewithsst
# you need price
def calculateSST(price):
    pricewithsst = price + (price*0.06)
    return pricewithsst

#this map func takes 2 parameter
#1st parameter is the function
#2nd parameter is the list
pricewithsst=map(calculateSST,prices)


'''
def map(func, values):
    result = []
    for value in values:
        result.append(func(value))
        return result
'''    
#################################################

fahrenheits = [32,33,34,35,36,37,38,39,40]
celcius = []
for fahrenheit in fahrenheits:
    celciusvalue = (fahrenheit-32) * 5/9
    celcius.append(celciusvalue)
print(f"celcius for loop {celcius}")

#using list comprehension
celcius = [(fahrenheit-32) * 5/9 for fahrenheit in fahrenheits]
print(f"celcius list comprehension {celcius}")

#using map class
def fahrenheitToCelcius(fahrenheits):
    return (fahrenheits-32)*5/9
celcius = map(fahrenheitToCelcius,fahrenheits)
print("celcius map: ", list(celcius))

######################################################################

multipleof3 = []
for number in range(1,50):
    if(number%3 == 0):
        multipleof3.append(number)

print("for loop multiple of 3",multipleof3)
multipleof3 = [number for number in range(1,50) if (number%3==0)]
print("multiple of 3 list comprehension", multipleof3)

#using filter class
def findMultipleOf3(number):
    return True if ( number % 3 == 0) else False

multipleof3 = filter(findMultipleOf3, range(1,50))
print(list(multipleof3))


######################################################################


numbers = [2,5,7,3,4,6,10,11,15,17,24,22]
oddnumber=[]
for number in numbers:
    if(number%2 !=0):
        oddnumber.append(number)
print(oddnumber)
oddnumber = [number for number in numbers if (number%2!=0)]
print("oddnum list comprehension",oddnumber)


#using filter class
def isOddnum(number):
    return True if (number %2 != 0) else False

oddnumber = filter(isOddnum, numbers)
print(list(oddnumber))

####################################################################33


sum=0
for number in range (1,10):
    sum += number
print ("sum",sum)
mean = 0
for number in range(1,11):
    mean = mean + number
mean = mean/len(range(1,11))
print ("mean",mean)

from functools import reduce
numbers = [1,2,3]

def findTotal(oldValue,currentValue):
    return oldValue + currentValue
print( reduce(findTotal, numbers))

"""
def reduce(func, number):
    sum = 0
    for number in numbers:
        sum = func(sum, number)
    return sum
"""

################################################

def factorial(oldValue,currentValue):
    return oldValue * currentValue
print( reduce(factorial, numbers,5))
#eva