import json
from pathlib import Path

fileName = "user_products.json"

if Path(fileName).exists():
    with open(fileName, "r") as file:
        productData = json.load(file)
else:
    productData = {"products":[]}


productName = input("Product name: ")
productPrice = int(input("Product price: "))
productAvailibilityInput = input("Product availibility : yes/no ").lower()
productAvailibility = True if productAvailibilityInput == "yes" else False
productWeight = int(input("Product weight: "))

product = {'name': productName,
                    'price' :productPrice,
                    'available':productAvailibility,
                    'weight': productWeight
}


productData["products"].append(product)

# print(productData)

with open ('user_products.json', 'w') as myFile:
    json.dump(productData, myFile, indent = 2)
    