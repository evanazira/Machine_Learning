#find the perfect factors of a number
'''
num = 1
count = 0

while count<4:
    proper_divisor = []
    sum = 0

    for i in range(1,num):
        if num % i == 0:
            proper_divisor.append(i)
    #print(proper_divisor)

    #find the sum of the perfect factors
    for factor in proper_divisor:
        sum = sum + factor
    #print(sum)
    
    if sum==num:
        print(f"The number {num} is a perfect number. Its perfect factor are {proper_divisor}")
        count += 1

    num += 1
    


num=1
count = 0
while count<4:
    primetest = (2**num) - 1

#N = int(input(""))
count = 0
num=2 #testlist for primenum

while(count < 4):
    isPrime = True
    
    for i in range(2,num):
     if (num %i==0):
       isPrime = False
       break
    
    if (isPrime==True):
        if((2**num) - 1)==num:
            print(num,end=" ")
            count += 1
    num += 1'''
a=(1,2,3)
b=('A','B','C')
c=zip(a,b)      #returns Zip Object
print(list(c))