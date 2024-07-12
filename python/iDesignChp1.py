#Q3
branding_expenses = int(input("Enter branding expenses\n"))
travel_expenses = int(input("Enter travel expenses\n"))
food_expenses = int(input("Enter food expenses\n"))
logistic_expenses = int(input("Enter logistics expenses\n"))

total_expenses = branding_expenses + travel_expenses + food_expenses + logistic_expenses

branding_percentage = (branding_expenses/total_expenses) *100
travel_percentage = (travel_expenses/total_expenses) *100
food_percentage = (food_expenses/total_expenses) *100
logistic_percentage = (logistic_expenses/total_expenses) *100

print(f"Total expenses : Rs.{total_expenses:.2f}")
print(f"Branding expenses percentage : {branding_percentage:.2f}%")
print(f"Travel expenses percentage : {travel_percentage:.2f}%")
print(f"Food expenses percentage : {food_percentage:.2f}%")
print(f"Logistics expenses percentage : {logistic_percentage:.2f}%")


#Q4

#Adult ticket = X + childeren ticket
#Senior ticket = 2 * children ticket
#Children ticket = ?
# Y = adult sale + children sale + senior sale
# 700 = [(10 + children ticket) * 5] + [children ticket* 2] + [(2 * children ticket) * 3]
# 700 = (50 + 5 children ticket) + 2 children ticket + 6 children ticket
# 700 = 50 + 13 children ticket
# Y = 50 + 13C
# C = (Y-50) / 13 


x = int(input("Enter the value of X\n"))
total_sale = int(input("Enter the value of Y\n"))

children_ticket = int((total_sale - 50) / 13) 
adult_ticket = int(x + children_ticket)
senior_ticket = int(2 * children_ticket)

print(f"Number of children ticket sold: {children_ticket}" )
print(f"Number of adult ticket sold: {adult_ticket}")
print(f"Number of senior ticket sold: {senior_ticket}" )


