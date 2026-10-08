products=["Laptop","Mouse","Keyboard","Monitor"]
print(products)

#indexing
print(products[0])
print(products[1])
print(products[2])

# Negative Indexing
print(products[-1])
print(products[-2])

#updating a particular element
products[1]="Wireless Mouse"
print(products)

#adding element at the end - append
products.append("Disk")
print(products)

#inserting element at a particular index
products.insert(1,"Led Monitor")
print(products)

#removing a element
products.remove("Led Monitor")
print(products)

#sorting
products.sort()
print(products)

#remove last element
products.pop()
print(products)