'''
principle = 1000
period = 1
rate = 6
simpleInterest = (principle * period * rate)/100
print("Simple Interest: ",simpleInterest)
'''
'''
def calculateSimpleInterest(principle, period, rate):
    simpleInterest = (principle * period * rate)/100
    return simpleInterest


#  and simpleInetrest in this fuction
# is the parameter that can be acess by the func only
def calculateTotalAmountToBePrinted (principle,simpleInterest):
    return principle + simpleInterest

principle = 1000
period = 1
rate = 6
result = calculateSimpleInterest(principle, period,rate)
# the principle and result is the argument 
# for func calculateTotalAmountToBePrinted
newresult = calculateTotalAmountToBePrinted(principle, result)

print("Simple Interest", result)
print("Total amount to be paid: ", newresult)
'''
class student:
    def __init__ (self):#method called constructor
        print("Object is created")

    #methods must have atleast 1 parameter
    def attendClass(self):
        print("Object started atttending the class")

    #this method have two parameter but ony projectname parameter must have argument
    def doProject(self,projectname):
        print("Object started doing the project", projectname)

    def attendExam(self, exam):
        grade = "A"
        return f"Object has attended the {exam} and obtained the score {grade} "

zul = student()
zul.attendClass()
zul.doProject("Pokemon")
print(zul.attendExam("Python102"))