#Given number is 97531
#i want you to reverse the number using only arithmetic operations
#expected resut is 13579

a0 = 97531
result = a0 % 10                 #--> to split the last digit and have the value 
a1 = a0 // 10                    #--> to have the quotient for the next division
print (result, a1)

result = (result * 10) + (a1%10) #--> 1*10 + 3
a2 = a1 // 10
print (result, a2)

result = (result * 10) + (a2%10) #--> 13*10 + 5
a3 = a2 // 10
print (result, a3)

result = (result * 10) + (a3%10) #--> 135*10 + 7
a4 = a3 // 10
print (result, a4)

result = (result * 10) + (a4%10) #--> 1357*10 + 9
a5 = a4 // 10
print (result, a5)

#Akmal solution
a0 = 97531
result = (a0 % 10)*10000  #--> to get the remaider to be the first number
result = result + ((a0 // 10) % 10) * 1000
result = result + ((a0 // 100) % 10) * 100
result = result + ((a0 // 1000) % 10) * 10
result = result + ((a0 // 10000 ) % 10) * 1
print (result)

#Other soltion
givenNumber = 97531
result = 0
result= result * 10 + givenNumber % 10 # 1
givenNumber //= 10         #9753
result = result*10 + (givenNumber % 10)
givenNumber //= 10         #975
result = result*10 + (givenNumber % 10)
givenNumber //= 10         #97
result = result*10 + (givenNumber % 10)
givenNumber //= 10         #9
result = result*10 + (givenNumber % 10)
givenNumber //= 10         #0
result = result*10 + (givenNumber % 10)

#other solution
givennumber = 97531
strgivennumber = str(givennumber)
print(int((strgivennumber[::-1])))


totalDay = 5
currentDay = 0
print (currentDay % totalDay)
print (1 % 5)
print (2 % 5)
print (3 % 5)
print (4 % 5)
print (5 % 5)


