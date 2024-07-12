name = "David"
batch = 101
fee = 1245.6578
inputstring = "Hello " + name + ", welcome to python class" + str(batch)
print(inputstring)

#alternative way
#special string called f string
inputstring = f"Hello {name}, welcome to python class {batch}"
print(inputstring)

#how much space is required
inputstring = f"Hello {name:40s}, welcome to python class {batch}"
print(inputstring)

#allign david to centre
inputstring = f"Hello {name:^40s}, welcome to python class {batch}"
print(inputstring)

#allign david to the right near to the comma
inputstring = f"Hello {name:>40s}, welcome to python class {batch}"
print(inputstring)

#padding characters (any character)
inputstring = f"Hello {name:*>40s}, welcome to python class {batch}"
print(inputstring)

#Trucate to 3 alphabet only
inputstring = f"Hello {name:.3}, welcome to python class {batch}"
print(inputstring)

#Number format (take 10 space)
inputstring = f"Hello {name:.3}, welcome to python class {batch:10d} in KL"
print(inputstring)

#Number format
inputstring = f"Hello {name:.3}, welcome to python class {batch:<10d} in KL"
print(inputstring)

#Number format (2 decimal point of fee with 10 space)
inputstring = f"Hello {name:.3}, welcome to python class {batch:<10d} in KL for RM {fee:10.2f}"
print(inputstring)

#binary value for batch 101
inputstring = f"Hello {name:.3}, welcome to python class {batch:b} in KL for RM {fee:10.2f}"
print(inputstring)

#hex value for batch 101
inputstring = f"Hello {name:.3}, welcome to python class {batch:x} in KL for RM {fee:10.2f}"
print(inputstring)

# value seperator for fee
inputstring = f"Hello {name:.3}, welcome to python class {batch:b} in KL for RM {fee:,.2f}"
print(inputstring)