# Python Functions

def greet():
    print("Hello, Chitra!")

greet()                  # Call function


# Function with parameter

def greet(name):
    print("Hello", name)

greet("Chitra")          # Pass argument
greet("Ram")             # Pass argument


# Function with multiple parameters

def add(a, b):
    print(a + b)

add(10, 20)
add(5, 15)


# Function with return value

def add(a, b):
    return a + b

result = add(10, 20)

print(result)            # Print returned value


# Other examples

def multiply(a, b):
    return a * b

print(multiply(5, 4))


# Function with default parameter

def greet(name="Chitra"):
    print("Hello", name)

greet()                  # Use default value
greet("Ram")             # Pass new value


# Function with multiple return values

def calculate(a, b):
    return a + b, a - b

addition, subtraction = calculate(10, 5)

print(addition)
print(subtraction)


# Other example

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Chitra", 18)
student("Ram", 20)


# Built-in functions

numbers = [10, 20, 30, 40, 50]

print(len(numbers))      # Number of items
print(sum(numbers))      # Sum of items
print(max(numbers))      # Largest value
print(min(numbers))      # Smallest value


# Other example

def square(number):
    return number * number

print(square(5))
print(square(10))