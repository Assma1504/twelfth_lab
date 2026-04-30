import json

with open('products.json','r') as myFile:
    fileProducts = json.load(myFile)
    # print(fileProducts["products"])
    for product in fileProducts["products"]:
        print(f'Name: {product["name"]}\nPrice: {product["price"]}\nWeight: {product["weight"]}\n{'available' if product["available"] else "Not available"}\n\n' )



