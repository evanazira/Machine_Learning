x = input("What is the size list: ")
listA = []
f_num = 30
s_num = 35
count1 = 0 #for the size of the list
count2 = 0 #for the 
count3 = 0
while count1<int(x):
    if (count1%2==0):
        f_num += count2
        listA.append(f_num)
        count2 += 8

    elif(count1%2!=0):
        s_num += count3
        listA.append(s_num)
        count3 += 6
    
    count1+=1
print(listA)

