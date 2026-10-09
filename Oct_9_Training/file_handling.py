# writing in a file
file = open("employees.txt", "w")

file.write("101,Aman,IT,75000\n")
file.write("102,Meera,HR,65000\n")
file.write("103,Rohan,Finance,70000\n")

file.close()

# reading the file
file = open("employees.txt", "r")
data = file.read()
print(data)
file.close()

# Other Operations
# line strip example
file = open("employees.txt", "r")
for line in file:
    print(line.strip())
file.close()

# writing a line in file
file=open("employees.txt", "a")
file.write("104,Sara,Sales,68000\n")
file.close()

# Unstructured Data -- Text,Audio,Video,PDF,Doc -- Azure Cloud
# Semi Structured Data -- JSON -- Mongo DB
# Structured Data -- Tables -- My SQL