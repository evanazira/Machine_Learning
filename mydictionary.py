#python dictionary is also called JSON in other programming language
# JavaScript Object Notation(JSON)
#Dictionary is also using {}
#the data is ordered
#the data is indexed by key (not by number)
#every single data is associated with a key 
# For example firstname is key and Peter is the data 
# Key cannot be duplicated, Data can be duplicated 
# It is modifieable
foreigner = {
    "firstname" : "Eva Nazira", 
    "lastname" : "Nazry Syah",
    "passportnumber" : "E4837589",
    "incometaxnumber" : "SG83494",
    "pcbamount" : 892,
    "lastmonth": 5,
    "lastyear" : 2024,
    "previousmonth" : [(4, 2024, 891), (3, 2024, 895),(2, 2024, 893),(1, 2024, 892)],
    "adress" : {
        "office" : {
            "street" : "IEG Campus, Jalan Sultan Ismail",
            "City" : "Kuala Lumpur"

        },
        "home" : {
            "street" : "1298,Jalan Pulai jaya 44, Bandar Pulai Jaya",
            "taman" : "Skudai"

        }
    },
    "contact" : "01124198078"

}

print("First name: ", foreigner["firstname"])
print("Last Name: ", foreigner["lastname"])
print("Passport Number: ", foreigner["passportnumber"])
print("Income Tax Number: ", foreigner["incometaxnumber"])
print("PCB Amount: ", foreigner["pcbamount"])
print("Last Month: ", foreigner["lastmonth"])
print("Last Year: ", foreigner["lastyear"])

#for item in foreigner ["previousmonth"]:
#item will hold a tuple(4,2024,891)
#howevr we know tuple is auto explodable
#as long as we have 3 variable we can explode and hold the 3 values
for month, year, amount in foreigner["previousmonth"]:
    print(f"Transaction: {month}-{year}   RM{amount}")

officeAdress = foreigner["adress"]["office"]
print("Street:", officeAdress["street"])
print("City: ", officeAdress["City"])
homeAdress = foreigner["adress"]["home"]
print("Street:", homeAdress["street"])
print("Taman: ", homeAdress["taman"])

#you can directly access the street as follows
office = foreigner["adress"]["office"]["street"]
print(office)

#sometimes we dont know the keys
print(foreigner.keys())
for key in foreigner.keys():
    #isinstance is a built in func to determine the type of the variable
    if(isinstance(foreigner[key], list)):
        for item in foreigner[key]:
            print(item)

    else:    
        print(foreigner[key])

#wher you use the method items you will get the key, value
for key, value in foreigner.items():
    print(key,value)

#how can i modify the dictionary
#since the key car does not exist in the dictionary it gets added automatically
foreigner["car"] = {
    "brand" : "Proton",
    "model": "saga",
    "carplate": "JUR 308"
}
foreigner["salary"] = 4890
print(foreigner)

#if i want ot modify the salary
#since the salary already there it modifies/updates the existing salary
foreigner["salary"] = 5120

print (foreigner)