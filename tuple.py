# Python Tuple

numbers = (10, 20, 30, 40, 50)

print(len(numbers))       # Number of items
print(numbers[0])         # First item
print(numbers[1:4])      # Slicing

print(numbers.count(20)) # Count item
print(numbers.index(30)) # Find index

# Tuple cannot be changed
# numbers[0] = 100       # This gives an error

# Other examples

marks = (67, 34, 98, 65, 80, 34)

print(marks)
print(marks.count(34))
print(marks.index(98))

names = ("Chitra", "Ram", "Sita")

print(names[0])
print(names[1:])