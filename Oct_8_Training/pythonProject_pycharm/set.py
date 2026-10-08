cities={"Hyderabad","Mumbai","Delhi","Chennai"}
print(cities)

# To add element
cities.add("Pune")
print(cities)

# To remove element use - .remove but if the specified element is not present it throw error
cities.remove("Mumbai")
print(cities)

# To remove without throwing any error if the specified element is not in the set
cities.discard("Delhi")
print(cities)

#Set does not allow the duplicates
city=[
    "Hyderabad",
    "Mumbai",
    "Delhi",
    "Chennai",
    "Hyderabad",
    "Mumbai",
    "Delhi",
]
unique_cities=set(city)
print(unique_cities)
