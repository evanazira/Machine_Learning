import json

try:
    with open('fruitsdictionaty.json') as filehandler:
        data = json.load(filehandler)
        for product in data:
            print(product["product"])
            print(product["quantity"])
            print(product["price"])

except Exception as e:
    print("Something went wrong",e)