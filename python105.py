#Q1
'''
for i in range(1,101):
    if (i%3==0 and i%5==0):
        print ("FizzBuzz")

    elif (i%3==0):
        print ("Fizz")

    elif (i%5==0):
        print("Buzz")
    
    else:
        print(i)

#Q2
number = int(input("Enter a number: "))
collatz_seq = [number]
next_num = number
while next_num!=1:
    if next_num%2==0:
        next_num = next_num/2
        collatz_seq.append(int(next_num))
        
    elif next_num%2 !=0:
        next_num = (3*next_num) + 1
        collatz_seq.append(int(next_num))


print(collatz_seq)

#Q3
n1 = int(input("Enter the 1st number: "))
n2 = int(input("Enter the 2nd number: "))
if(n1>n2):
  (A , B) = (n1 , n2)
elif(n2>n1):
  (A , B) = (n2 , n1)
print(A,B)

while B!=0:
   quotient = A // B
   remainder = A % B
   A = B
   B = remainder
   print(A,B)

#Q4
import random
print("Rock     Paper     Scissor")
userChoice = input("Enter your choice: ")
programChoice = random.randint(1,3)

if(userChoice=="rock"):
  userChoice = "Rock"
elif(userChoice=="paper"):
  userChoice = "Paper"
elif(userChoice=="scissor"):
  userChoice = "Scissor"

if(programChoice==1):
  programChoice = "Rock"
elif(programChoice==2):
  programChoice = "Paper"
elif(programChoice==3):
  programChoice = "Scissor"
print("The program choice: ",programChoice)

#to dettermine the winner
#scissor win with paper
#paper win with rock
#rock win with scissor
while userChoice=="Rock" or userChoice=="Paper" or userChoice=="Scissor":
  if(userChoice=="Rock" and programChoice=="Scissor" or userChoice=="Paper" and programChoice=="Rock" or userChoice=="Scissor" and programChoice=="Paper"):
    print("You WIN and The program LOSE")
    break

  elif(programChoice=="Rock" and userChoice=="Scissor" or programChoice=="Paper" and userChoice=="Rock" or programChoice=="Scissor" and userChoice=="Paper"):
    print("The program WIN and You LOSE")
    break

  elif(userChoice==programChoice):
    print("TIED")
    break
else:
  print("Error")'''
  
#Q5
import random
randomNum=random.randint(1,100)
numGuess = int(input("Enter the guess number: "))

while numGuess != randomNum:
    if(numGuess > randomNum):
        print("The guessed number is too high")

    elif(numGuess < randomNum):
        print("The guessed number is too small")
    
    numGuess = int(input("Enter new guess number: "))

else:
    print("The guessed number is correct!", randomNum)

#Q6
