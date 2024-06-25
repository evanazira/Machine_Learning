
#when we call python to executed our program we camn pass our value to our program in the command line which also called command line argument
#sys.argv give us a list which contain command line argument and passed to python
#in the list you can see the item at position 0 is program name itself
#the argument is in string
#the argument is seperated by space

import sys
cmdargument = sys.argv #we are using dot operator to acess the variable which inside the module
print (cmdargument)

#find the total of all the argument
#if we know the toal argument we can ddo it like this
#total = int(cmdargument[1]) + int(cmdargument[1])
#in this case we have to use loops
total=0
for number in cmdargument[1:]:
    total = total + int(number)

print(total)