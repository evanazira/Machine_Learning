'''''
def sayHelloWorld():
    print("Hello World")


#func are created using keyword def followed by func name 
#which again followed by paranthesis ()
#which again followed by colon :

#how to calling a func
sayHelloWorld()

def greeting(name):
    print("Good morning," , name)


greeting('eva')
##################################################################
def total(x, y, z): #in the () is the parameter
    result = x+y+z
    print("Result = ", result)

total(10, 20, 30) #in the () is argument
##################################################################

def buylunch(makan,minum):
    price = []
    for food in makan:
        if (food=="nasi"):
            price.append(2.80) #the append will add the price in the list

        elif(food=="sayur"):
            price.append(1.50)

    for drinks in minum:
        if(drinks=="milo"):
            price.append(3.00)


    #print(makan,minum, price)
    return price #to return price to user
    

itemprice = buylunch(["nasi", "sayur"], ["milo"])
pay = 0
for price in itemprice:
    pay += price
print(f"Your total is RM {pay}")
##################################################################
def simpleInterest(principle, period, rate):
    interest = (principle* period * rate) / 100
    return[interest, principle,period, rate]

print("The simple interest, principle, period, rate", simpleInterest(1000,1,6))

##################################################################
def participant(name1, name2, name3):
    name1 = name1 + "data science"
    name2 += "data science"
    name3 += "data Science"

    return name1, name2, name3

result = participant("John--", "Eva--", "Amal--")
print(result)
#################################################################
def calculatesimpleInterest(principle, period=1, rate=6):
    interest = (principle* period * rate) / 100
    return[interest, principle,period, rate]

print(calculatesimpleInterest(1000,2))
print(calculatesimpleInterest(1000))
print(calculatesimpleInterest(principle=1000, rate=5))


##############################################################
def findtotal(givennumber):
    total =0
    for givennumbers in givennumber:
        total = total+ givennumbers
        return total
    
    
print(findtotal([10, 20, 30]))
print(findtotal([10, 20, 30, 40, 50, 60]))

def listSixLetterfruit(*fruits):
    for fruit in fruits:
        if len(fruit)==6: print(fruit)

listSixLetterfruit ("Appkl", "orenge","manggo", "banana","durian", "grapes")

###################################
def listSixLetterfruit(*fruits):
    for fruit in fruits:
        print(fruits)

listSixLetterfruit ("Appel",20, 4.2, "orenge",40, 1.2)
'''
def sum(a,b):
    return a+b

def minus(a,b):
    return a-b

def arithmetic(func,a,b):
    return func(a,b)

def mul(a,b):
    return a*b

print(arithmetic(sum,20,10))


