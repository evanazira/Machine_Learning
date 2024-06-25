#tuple is nothing but readonly list
# tuple uses[]
# cannot modifieable(cannot append, edit,and delete)
#ordered(the items retains its position)
#indexed(0,1,2,3,4....)
#allows duplicate

x = (10,20,30,40,50,60,70)
print (x)
print(type(x))

#selection and indexing refer to variable2.py
print(x[0])

#it is not modifiable
fruits = ("apple", "orang", "apple", "mango", "apple")
x.count("apple")
print (x)

#####
#this function will change the original list in x
def total(*number):
    number[2] = 35
    result = 0
    for numbers in number:
        result = result +numbers
    return result

x = (10,20,30,40,50)
print(x)
print(total(x))
print(x)

#to avoid this, you pass the list to the tuple class it will return tuple object
#x = tuple(x)
print(x)

x = (10)
print(type(x)) #suppose to be tuple but the python will prioritise expression 
