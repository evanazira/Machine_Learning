#there are 4 diff types buildin data structure in python
#they are list, tuple, set, and dictionary

#list uses[]
#modifieable(append, edit,and delete)
#ordered(the items retains its position)
#indexed(0,1,2,3,4....)
#allows duplicate
'''
fruits = ["apple", "orange", "mango","banana","grapes"]
print(fruits)

fruits.append("durian")
print(fruits)

fruits.insert(1,"rambutan")
print(fruits)

fruits.insert(3, "cempedak")
print(fruits)

fruits.insert(5,"dummy")
print(fruits)

#update
fruits[5] = "mangosteen"
print(fruits)

#remove
fruits.remove("durian")
print(fruits)

#remove the last item 
fruits.pop()
print(fruits)

greeting = "good morning"
del greeting
del fruits[3]
print (fruits)
fruits.clear()
print(fruits)
del fruits

fruits = ["apple", "orange", "mango","banana","grapes"]
print(fruits.index("mango"))

newfruit = fruits[2:]

print(fruits.index("mango")+1) #skip 1 index 
print(newfruit)

print(list(enumerate(fruits)))
for item in enumerate(fruits):
   # print (item[0])
    #print(item[1])
    if item[1] =="mango":print("mango is in postion : ", item [0])

print("total number of apple = ", fruits.count("apple"))

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

for fruit in fruits:
    print()
'''
#shallow copy
x = [10,20,30,40,50]
y = x
print(x)
print(y)
print("-"*40)
x[2]=35
print (x)
print(y)

#deep copy
x = [10,20,30,40,50]
y = []
for i in x:
    y.append(i)
print("=" *40)
print (x)
print(y)
print("-"*40)
x[2]=35
print (x)
print(y)

#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#x#
#fruits in an instance of a lis
#technically the object are createsd by calling the class
x= list([15,25,35,45,55])
print(x)
#however in python to create list instead of using class they let you to usee []
x = [12,22,32,42,52]
print(x)

#in python to invoke or call the operator we use is() parenthesis(round bracket)
#() also used in expression
#to call buid in func print() sum() id()
#to create object we call the class int() type() int() float() list()
#to call func inside  a module sys.path()
#to call menthod in a object "Televisyen".split()