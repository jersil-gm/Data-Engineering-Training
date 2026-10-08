# Dictionary is used when we need to store data in key value pair
product={
    "product_id":101,
    "product_name":"Mobile",
    "Category":"Electronics",
    "price":65000
}

print(product)

#Access
print(product["product_name"]) # this will crash if there is no specified key

# Access without error - Get
print(product.get("brand"))

# To update a value
product["price"]=70000
print(product)

# To add a new key value pair
product["Stock"]=20
print(product)

# To Remove
product.pop("Category")
del product["price"]
print(product)