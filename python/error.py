# x = 11

#4
# #syntex error
# if (x % 2 == 0):
# print(f"Given number is {x}")
# print("Even number")

# #logical error
# if (x % 2 == 0):
#     print(f"Given number is {x}")
# print("Even number")

#runtime error
#when the user is enter different data type
try:
    principle = int(input("Principle:"))
    period = int(input("Period:"))
    rate = int(input("Rate:"))
    interest = (principle*period*rate)/100
    print("Interest Amount", interest)

except ValueError:
    print("Error. The amount must be an integer")
    
except Exception as e:
    print("SoMEthing went wrong: ", e)

else:
    #the code inside the else block gets execute only when there are no erroe
    print("All is well")

finally:
    # the code inside this block will always get executed
    # regardless of whether an error occur or not

    print("Thank you")

# period = int(input("period: "))
# rate = int(input("rate: "))
# interest = int(input("interest: "))