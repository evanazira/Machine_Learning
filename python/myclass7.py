#multiple inheritnce
class card:
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside Card class")

class ATMCard(card):
    def __init__(self):
        pass
    # def doSomething(self):
    #     print("Inside ATM class")

class DebitCard(card):
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside Debit class")

class creaditCard(card):
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside Creadit Card class")

class BankCard(ATMCard,DebitCard,creaditCard):
    def __init__(self):
        pass
    def doSomething(self):
        super().doSomething()
        
card = BankCard()
card.doSomething()

print(BankCard.__mro__)

class myclass:
    pass

class noObjectClass():
    pass
test = noObjectClass()
print(test)