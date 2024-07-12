#method are nothing but func inside the class
#method take atleast 1 parameter (self)
#pyhton uses this to pass the instance

class calculator:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    
    def subtract(self):
        return self.x - self.y

mycalculator = calculator(10,20)
print (mycalculator.add())
print (mycalculator.subtract())

class utility:
    def addition(x,y):
        return x+y
    
    def subtraction(x,y):
        return x-y


print (utility.addition(100,200))

class Customer:
    def __init__(self, firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def getFullName(firstname,lastname):
        return firstname + lastname
    
    def __str__(self):
        return Customer.getFullName(self.firstname, self.lastname)
    
myCustomer = Customer("John", "David")
print(myCustomer)