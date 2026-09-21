# Python Dictionary

student = {
    "name": "Chitra",
    "age": 18,
    "course": "BCA",
    "city": "Kathmandu"
}

print(len(student))       # Number of items

print(student["name"])    # Access value
print(student["age"])     # Access value

student["age"] = 19       # Change value
student["phone"] = "98XXXXXXXX"  # Add item

print(student)


# Other examples

marks = {
    "Math": 67,
    "English": 80,
    "Account": 75,
    "Economics": 65
}

print(marks["Math"])      # Access Math marks
print(len(marks))         # Number of items

marks["Math"] = 70        # Change value
marks["Computer"] = 85    # Add item

print(marks)


# Dictionary methods

student = {
    "name": "Chitra",
    "age": 18,
    "course": "BCA"
}

print(student.keys())     # Show all keys
print(student.values())   # Show all values
print(student.items())    # Show key-value pairs

student.pop("age")        # Remove item

print(student)


# Other example

names = {
    "student1": "Chitra",
    "student2": "Ram",
    "student3": "Sita"
}

names["student4"] = "Hari"    # Add item
names.pop("student2")         # Remove item

print(names)