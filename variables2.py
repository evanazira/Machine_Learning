#we learn how to assign to multiple values to multiple variable in a line
#x,y = 10,11
#how to assign multiple values in a single variable
# let say we want to go to shopping,
#and we have 10 items to buy
# that does no mean we need to create 10 variablrs and assign them to each variable
#we can use new data structure called list
#in other programming language, it called array

fruits = ["appel","orange","mango","banana","grape"]

#indexing and selection
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

print(fruits[4])
#how many items are there in the list
#there isis a built func len
print("NUMBER OF ITEMS WE HAVE :", len(fruits))

#how to find the maximum index
print("maximum index:", len(fruits) - 1)
      
#does the index must be a positve number?
#not necessaryly because it can be in -ve number(in python)
print (fruits[-1])
print (fruits[-2])
print (fruits[-3])
print (fruits[-4])
print (fruits[-5])

#range start_index:end_index
#in python when we refer to range, the end_index is not included
print(fruits[1:3]) #->only orange untill mango....banana is not included
#the end_index is not included

#to get until banana
print(fruits[1:4])

#if we did not mention the start index, it will start index as 0
print(fruits[:4])
#if we did not mention the end index, it will print until last index

#in the range we can have the 3rd numbeer which represent the step value

fruits = ["appel","rambutan","orange","durian","mango","cempedak","banana","mangosteen","grape"]
#          -9         -8        -7       -6      -5        -4        -3        -2         -1
print(fruits[0:9])
print(fruits[0:9:2]) #->step up by 2
print(fruits[0:9:3]) #->step up by 3  ->the end_index will not be executed/printed

print(fruits[-5:-1]) # 'mango','cempedak','banana','mangosteen'  -> the end_index is excluded
print(fruits[-1:-5]) #-1>-5 start index is greater than end_index result in empty list
#this is bcs by default step up 1 -1 +1
print(fruits[-1:-5:-1]) #here item at -5 is excluded
#which means if you want to reverse entire the list
print(fruits[::-1]) #if nak start from back and call semua items
#tak perlu mention start and end index. just mention steup up argument
