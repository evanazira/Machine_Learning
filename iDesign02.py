
"""
tic_num = int(input("Enter your ticket number: "))

if (tic_num%10==3 or tic_num%10==8):
    print("Lucky Winner")

else:
    print("Not a Lucky Winner") 
"""'''''
########################
tic_char = input("")
if(tic_char == 'E' or tic_char=='e'):
    print("Early Bird Ticket")

elif(tic_char == 'D' or tic_char=='d'):
    print("Discount Ticket")

elif(tic_char == 'V' or tic_char=='v'):
    print("VIP Ticket")

elif(tic_char == 'S' or tic_char=='s'):
    print("Standard Ticket")

elif(tic_char == 'C' or tic_char=='c'):
    print("Child Ticket")

'''
#########################
'''
X = int(input(""))
num_tic = int(input(""))

total = X * num_tic

if (num_tic>=50 and num_tic<=100):
    print(f"{total*0.9:.2f}")

elif (num_tic>=101 and num_tic<=200):
    print(f"{total*0.8:.2f}")

elif (num_tic>=201 and num_tic<=400):
    print(f"{total*0.7:.2f}")

elif (num_tic>=401 and num_tic<=500):
    print(f"{total*0.6:.2f}")

elif (num_tic>500):
    print(f"{total*0.5:.2f}")

else:
    print(f"{total:.2f}")
#############################################################
    '''''''
basic_salary = int(input(""))


if(basic_salary < 15000):
    HRA = 0.15 * basic_salary
    DA = 0.9*basic_salary

elif(basic_salary>=15000):
    HRA = 5000
    DA = 0.98*basic_salary

gross_salary = basic_salary + HRA + DA
print(f"{gross_salary:.2f}")
##############################################################
'''
factor = input("")
factor = factor.split(" ")

HF = int(factor[0])
SpF = int(factor[1])
SdF = int(factor[2])

if (HF > 50 and SpF>60 and SdF>100):
    Grade = 10

elif(HF > 50 and SpF>60):
    Grade = 9
    
elif(SpF>60 and SdF>100):
    Grade = 8

elif(HF>50 and SdF>100):
    Grade = 7

elif (HF>50 or SpF>60 or SdF>100):
    Grade = 6

else:
    Grade = 5

print(Grade)

