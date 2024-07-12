#aida question
#any/all (built-in func)
#they take boolean list as parameter
#[True, True, False, True, False, False]
givenNumber =  11
divisor = range(2,givenNumber)
if(len([mynumber for mynumber in divisor if (givenNumber %mynumber==0)])==0):
    print("prime number")

else:
    print ("Not prime mumber")

if any ([givenNumber %mynumber==0 for Number]):
print