#Is -A relationship
#Alumni Is- A Student
#Student is the parent for Alumni
class Student:
    def __init__(self, firstname, lastname): #__init__ for initializing all variable 
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = ""

#Alumni extends Student calss
class Alumni(Student):
    def __init__(self, firstname, lastname, alumninumber):
        #calling the __init__method statically
        #Student.__init__(firstname, lastname)#this is one way we create parent in child
        super().__init__(firstname,lastname)
        self.alumninumber = alumninumber


    def __str__(self):
        return f"First Name: {self.firstname}\nLast name: {self.lastname}\nIC Number: {self.icnumber}\nAlumni Number: {self.alumninumber}"


#we have created an object of Alumni class
alumni = Alumni("Eva","Nazry", "1917904")

#alumni = Alumni()
print(alumni)