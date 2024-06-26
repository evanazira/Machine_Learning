#func can have inner func
def sun(a,b):
    return a+b

x=10

#anonymous func assigned to a variable
'''
sum = def (a,b):
    return a+b
'''
def authenticate(username,password):
    #we have created an inner func
    def calculateSI(principal,period, rate):
        #def something():
        #    pass
        result = (principal *period*rate)/100
        return result
        
        #something()

    if (username=="admin" and password == "pwd123"):
        #since calculateSI func inside the authenticate func
        #we can call the func here
        #print("simple interest",calculateSI(1000,1,6))
        #instead of calling calculateSI
        #let us return the inner func calculateSI
        return calculateSI#address of the function is

func = authenticate("admin", "pwd123")
print("Simple Interest: ", func(1000,1,6))# only if the authenticate is rturn the other func (return calculateSI)
print("Simple Interest: ", authenticate("admin","pwd123")(1000,1,6))#alternative to the 2 above line

add = lambda a,b : a + b
#using normal func
fahrenheitValues = [32,33,34,35,36,37,38,39,40]
def fahrenheitToCelcius(fahrenheitValue):
    return (fahrenheitValue - 32)*5/9

celciusValues = map(fahrenheitToCelcius, fahrenheitValues)
print(list(celciusValues))

'''
using lambda func
step 1:create anaonymous func
def (fahrenheitValue): return (fahrenheitvalue - 32) * 5/9
step2: assign it to a variable
fahrenheitToCelcius = def(fahrenheitValue): return (fahrenheitValue - 32)*5/9
step 3: rename def to lmbda
fahrenheitToCelcius = lambda(fahrenheitValue): return (fahrenheitValue - 32)*5/9
step 4: remove() at parameter and return keyword
fahrenheitToCelcius = lambda fahrenheitValue : return (fahrenheitValue - 32)*5/9
'''
celciusValues = map(fahrenheitToCelcius, lambda value:(value - 32)*5/9)
print(list(celciusValues))

