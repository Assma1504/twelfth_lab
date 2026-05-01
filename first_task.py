import json

with open('products.json','r') as myFile:
    productsFile = json.load(myFile)
    # print(productsFile["products"])
    for product in productsFile["products"]:
        print(f'Name: {product["name"]}\nPrice: {product["price"]}\nWeight: {product["weight"]}\n-{'available' if product["available"] else "Not available"}\n\n' )



