# Python Lists

numbers = [10, 20, 30, 40, 50]

print(len(numbers))       # Number of items

numbers.append(60)       # Add item
numbers.remove(20)       # Remove item
numbers.insert(1, 25)    # Add at index 1
numbers.sort()            # Sort list

print(numbers)

# Other examples

marks = [67, 34, 98, 65, 80, 34]

print(marks[0])           # First item
print(marks.count(34))    # Count 34

marks[0] = 70             # Change item
marks.pop(2)              # Remove item at index 2

print(marks)

names = ["Chitra", "Ram", "Sita"]

names.append("Hari")
names.remove("Ram")

print(names)