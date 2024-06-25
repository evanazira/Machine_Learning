#Exmples 1
print("It's saturday today")
#cannot be --->print('it's staurday today'), must use different start and end quote that is different with the string's value

#Example 2
age = 24
name = 'Eva'
#print(name + age)--->error because of diff data type
print(f"{name} you are {age} years old")

#Example 3
# any input will give you str data type
#casted the input data type from str -> number
age_this_year = int(input("Enter your age in 2024: ")) 
month = age_this_year * 12 - 6
print(f"You have lived for {month} month")

#Boolean




#Input
age = input("Enter your age: ") #any input will give a string
print(age)
print(type(age)) #-> type: str

age = int(input("Enter your age: ")) #any input will give a string #in the brackets will be perfomed first
print(age)
print(type(age)) #-> type: int
