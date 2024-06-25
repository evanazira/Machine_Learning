num = 4+3%5
print(num)

a = 16
b = 15
num1 = float(22//3+3/3)
print(num1)

x=5
y=10
x = x ^ y
y = x^y
x = x^y
print("X=%d, Y=%d"%(x,y))

x=5
k= x+6j
print("Real part: %d\nImaginary part: %d"%(k.real,k.imag))


x=10
print ("Complex Number:",complex(x))

x = 'B'
print ("ASCII value:",ord(x))

x=15
print("Octal Value:",oct(x))
print("Hexadecimal Value:",hex(x))

a = 8+4j
print (a, "is complex number?",isinstance(a,complex))
n = 80
print ("Character :",chr(n))

'''
total = 1+2+3+4+\5+6+7
print(total)
'''

S="Hello"
print('e'in S)
print('p' in S)

x = True
y = False
z = False
if x or y and z:
               print("Hello")
else:
              print("World")

x = True
y = False
z = False
if not x or y:
               print(1)
elif not x or not y and z:
               print(2)
elif not x or y or not y and x:
              print(3)
else:
              print(4)

if (10 < 0) and (0 < -10):
                          print ("A")
elif (10 > 0) or False:
                          print ("B")
else:
                          print ("C")