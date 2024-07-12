# set uses {}
# modifieable( append, edit,and delete)
# unordered(the items does not retains its position)
# not indexed(do not have 0,1,2,3,4....)
# does not allows duplicate
x = {10,20,30,10,40,50,20,60,70}
print(x)

for i in x:
    print(i)


#modifieable
fruit = {"apple","orange", "mango" }
print(fruit)
fruit.add("durian")
print(fruit)

#to delete
fruit.remove("orange")
print(fruit)

#.pop randomly remove an item
fruit.pop()
print(fruit)

# if you wnat to update an item
# 1) remove the item
# 2) add the item
fruit=["apple","orange","apple","mango","banana","apple"]
uniquefruit = set(fruit)
print(uniquefruit)

overseafruit = {"apple","orange","mango", "banana", "grapes"}
localfruit = {"durian","rambutan", "cempedak","banana","mangosteen"}
print(overseafruit.union(localfruit))
print(overseafruit.intersection(localfruit))
print(overseafruit.difference(localfruit))
print(localfruit.difference(overseafruit))

favfruits = {"durian","rambutan","mangosteen"}
print(favfruits.issubset(localfruit))
print(localfruit.issuperset(favfruits))
print(favfruits.isdisjoint(overseafruit))

content = """ “Immediate action required!” or “Your account has been compromised!” 
— sounds pretty urgent, right? But that’s exactly what phishers want. 
They use urgent or threatening language to make you react without thinking.
For example, you might see phrases like, “Your account password has expired, 
update now before you lose access to your account” or “Attempt to deliver your package unsuccessful. 
Please update your information within the next 24 hours.” """
words = content.split()
cleanwords = []
for word in words:
    #word is instance of string class or word is a string object
    #remove is a method inside the word object
    #remove takes 2 arguments. first arg is used to find
    #secong arg is used to replace
    word = word.replace(",", "")
    word = word.replace(".","")
    word = word.lower
    cleanwords.append(word)
    
print(cleanwords)
print("original words: ",len(words))

uniqueword = set(words)
print(len(uniqueword))
print(uniqueword)

