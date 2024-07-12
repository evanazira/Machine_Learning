# write a program to find whether the given number is positive, negative or zero
#write a program to find whether our bussiness is making profit, loss or breakeven

expenses= 1000
sales = 1100

#Objective 1: Just say whether we are making profit (single condition)
if(sales>expenses):
    print("You are making profit")

#objective 2: Say whether we are making profit or loss (2 condition)
if(sales > expenses):
    print("We are making profit")
else:
    print("We are making losses")

#objective 3: Say whether we are making profit or loss or breakeven (3 condition)
if(sales > expenses):
    print("We are making profit")
elif (sales == expenses):
    print("We are breakeven")
    
else:
    print("We are making losses")

print("Thank You")

#if the statement to be executed is a single statement,
#  then we can write the if and statement in 1 line

#find whether the given number is even
givennumber = 5
if(givennumber%2==0): print("Even number")

#only if you have only 1 block of code
print("Even number") if(givennumber%2 == 0) else print ("Odd number")
print("+ve")if(givennumber>0) else print("-ve") if (givennumber<0) else print("zero")