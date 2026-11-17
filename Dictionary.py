# creation of Dictionary 
user={

    "Name":"charan",
    "Age":23,
    "Designation": "IT Intern"
}

# print(user)

# Accessing Values
student={
    "Name":"charan",
    "Age":23
}

# print(student["Name"])
# print(student["Age"])

# Adding elements

data={}

data["name"]="usha"
data["age"]=23

# print(data)

# Updating elements

update={
    "Name":"charan",
    "Age":22
}

update["Age"]=23

# print(update["Age"])

# Checking whether a key exists
numbers={
    2: 0,
    7: 1
}

# print(2 in numbers) # True
# print(5 in numbers) # False

# Understanding dictionary lookup
'''number={
    2: 0,
    7: 1,
    11: 2
}

if 7 in number:
    print("Found")
else:
    print("Not Found")  '''

# Dictionary operations 
# ==> len() counts Key-value pair
data1={
    "name":"charan",
    "age":22,
    "city":"Hyderabad"
}

print(len(data1))

# ==> del delete an element

data2= {"a":10,"b":20}
del data2["a"]
print(data2)