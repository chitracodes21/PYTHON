# Python Sets

numbers = {10, 20, 30, 40, 50}

print(len(numbers))       # Number of items

numbers.add(60)           # Add item
numbers.remove(20)        # Remove item
numbers.discard(30)       # Remove item safely

print(numbers)


# Other examples

marks = {67, 34, 98, 65, 80, 34}

print(34 in marks)        # Check if 34 exists
print(len(marks))         # Number of items

marks.add(90)             # Add item
marks.remove(65)          # Remove item

print(marks)


# Set operations

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))         # Combine both sets
print(A.intersection(B))  # Common items
print(A.difference(B))    # Items only in A


# Other example

names = {"Chitra", "Ram", "Sita"}

names.add("Hari")
names.remove("Ram")

print(names)