#polymorphism

class Gender:
    def __init__ (self):
        pass
    def doCarryObjects(self):
        pass
class Male(Gender):
    def __init__(self):
        pass

    def doCarryObjects(self):
        print("Carry Heavy Objects")

class Female(Gender):
    def __init__(self):
        pass

    def doCarryObjects(self):
        print("Carry Ligrht Objects")

def getGender(name):

    if "Bin" in name:
        return Male()
    else:
        return  Female()
gender = getGender("Nazry Syah Bin Eshak")
gender.doCarryObjects()
print(type(gender))