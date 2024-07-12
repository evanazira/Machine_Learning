def add(a,b):
    result= a+b
    return result

x = 10
def printX():
    print("inside the func printX",x)

printX()
print(x)

def modifyX():
    #this func will not modify x in the main
    x = 15
    print("inside the func modifyX", x)
    

modifyX()
print(x)
#if you really want to modify the variable in the global context
#the function must return the value 
#which again must be assigned to the global variable
def traditionalModifyX():
    x =12
    return x

x = traditionalModifyX()
print (x)

def pythonModifyX():
    global x
    x = 25
    print("Inside the function(pythonModifyX): ", x)

pythonModifyX()
print(x)

def simpleInterest(principle,period,rate):
    result = 0
    def printSimpleInterest():
        nonlocal result
        print("Print Simple interest:",result)
        print("Period: ",period)
    result = (principle * period * rate)/100
    printSimpleInterest()
    print("Result:", result)


simpleInterest(1000,1,6)
#summary
#global keyword allow the func to modify 
# the variable in the main/global contex
#the local keyward allow the inner func to modify 
# the variable which is  in the outer function contex (parent func)

fruit = "apple"
def myfunction():

    #to solve the problem of variable fruit not created locally, we create the variable with empty value
    fruit = ""
    #in this case the variable is suppose to be created locally
    print(fruit)
    #in this case we are reffering to a variable which is not initialized
    fruit = "orange"
    print(fruit)

myfunction()