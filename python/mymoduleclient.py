#1st method
'''
import mymodule

print("Interst: ", mymodule.simpleInterest(1000,1,6))
'''

#second method
#disadvanatge: if you want to import more then 1 function you have to explcitly say it
'''
from mymodule import simpleInterest
print("Interest: ", simpleInterest(1000,1,6))
print("result: ", add(10,20)) #cannot use this
'''

#third method
from mymodule import *
#this import * will bring all the func available to use
print("Interest: ", simpleInterest(1000,1,6))
print("result: ", add(10,20))