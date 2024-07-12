#Has-A relationship


class Passport:
    def __init__(self, country, passportnumber): #__init__ for initializing all variable 
        self.country = country
        self.passportnumber = passportnumber

    def __str__(self):
        return f"Country: {self.country} \nPassport Number: {self.passportnumber}"


class customer:
    def __init__(self, firstname, lastname): #__init__ for initializing all variable 
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = ""
        self.passport = ""

    def __str__(self):
        message = f"First Name: {self.firstname}\n"
        message = message + f"Last Name: {self.lastname}\n"
        message = message + f"IC Number: {self.icnumber}\n"
        if (self.passport != None):
            message = message + self.passport.__str__()
        return message


peter = customer("Peter","Parker")
peter.icnumber = "000321011676"
passport = Passport("UK","E0100333")
peter.passport = passport
print(peter)
print(peter.__dict__)

eva = customer("Eva","Nazry")
eva.icnumber = "000321011668"
passporteva = Passport("Malaysia","00032101668")
eva.passport = passporteva
print(eva)
print(eva.__dict__)