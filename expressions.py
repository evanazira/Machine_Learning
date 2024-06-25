#arithmatic Operators
x = 7
y = 2
#print function takes expressions as an argument
#result = x+y
#print("Addition: ", result)
print("Addition: ", x + y)
print("Subtraction: ", x - y)
print("Multiplition: ", x * y)
print("Division: ", x / y)

print("Quotient: ", x // y)
print("Remainder: ", x % y)

print("Exponent: ", 10**3)
print("What is the max num in a 64 bit env: ", (2**64)-1)

#Assignment Operator
#increament
x = 0
x += 1 #x = x + 1
#y= mx+c
#y= x**2 + 2*x +3
x+=2
x+=5

x+=x+1
x = 108 + (108+1)
x=217

x += 1
x -= 1
x /= 1
x *= 1
x //= 1
x %= 1

#how to assign more than one value to more than one variable in onle line statement
x , y = 101+1 , 102+1
x,y = x+1 , y+1
print(x,y)

#Comparison Operator
myHeight = 5.2
yourHeight = 5.3
mysisterHeight = 5.2

#TRUE statement
print(yourHeight > myHeight) #greater than
print(myHeight==mysisterHeight) #equals to
print(mysisterHeight < yourHeight) #less than
print (mysisterHeight!=yourHeight) #not equal to

print (yourHeight>= myHeight) #greater than or equals to
print(myHeight >=mysisterHeight)#greater than or equals to

print(myHeight<=yourHeight) #less than or equals to
print(mysisterHeight<=myHeight)#less than or equals to

#Logical Operator
a = 21 #when a=7
b = 14
c= 7 #when c=21

print (a>b and a>c) #a is the greatest
print(c<a and c<b) #c is  the smallest
print((b<a and b>c) or (b>a and b<c)) #b is the middle number

#Truth table
#Negation Operator (NOT)
print (not (a>c)) #False
print (not(a<c)) #True

#XOR (^)
print("XOR: ", (a>c) ^ (a>b)) #false