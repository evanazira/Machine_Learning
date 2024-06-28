class student:

    #usually init method is used to declare properties
    #1) Properties are nothing but variables but inside class
    #2) alwways prefix by the first variable
    #3) if not declare with prefix, it will become jut a local variable innside the method
    # it is  a propertie if it attach with the prefix 
    def __init__ (self, firstname, lastname, icnumber):#method called constructor
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = icnumber
        self.program = ""
        self.address = ""
    #methods must have atleast 1 parameter
    def attendClass(self):
        print(f"{self.firstname} {self.lastname} started atttending the class")

    #this method have two parameter but ony projectname parameter must have argument
    def doProject(self,projectname):
        print(f"{self.firstname} {self.lastname}  started doing the project", projectname)

    def attendExam(self, exam):
        grade = "A"
        return f"{self.firstname} {self.lastname} has attended the {exam} and obtained the score {grade} "
    
    def info(self):
        print("First Name: ", self.firstname)
        print("Last Name: ", self.lastname)
        print("IC Number: ", self.icnumber)

        #here program is a local variable created inside the method
        for program in self.program:
             print ("Program: ",program)
        print("Address: ")
        print(self.address["Street"])
        print(self.address["Area"])
        print(self.address["Poscode"])
        print(self.address["State"])
        print(self.address["Country"])

    def __str__(self):
        return f"""
        First Name: {self.firstname}
        Last Name: {self.lastname}
        IC Number: {self.icnumber}
        """


zul = student("Eva","Nazry","000321-01-1676")
zul.attendClass()
zul.doProject("Pokemon")
print(zul.attendExam("Python102"))


zul.program = ["mechatronics","Engineering","AI"]
zul.address = {
"Street": "1298,Jalan Pulai Jaya 44,",
"Area":"Bandar Pulai Jaya",
"Poscode" : "81300",
"State" :"Johor",
"Country": "Malaysia"


}
zul.info()
print(zul)