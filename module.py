# Working with Modules in Python

import math

print(math.sqrt(25))          # Square root
print(math.factorial(5))      # Factorial


# Using functions from a module

import math

print(math.sqrt(16))
print(math.factorial(5))


# Importing a specific function

from math import sqrt

print(sqrt(25))


# Importing multiple functions

from math import sqrt, factorial

print(sqrt(36))
print(factorial(5))


# Using an alias

import math as m

print(m.sqrt(49))


# Other examples

import random

number = random.randint(1, 10)

print(number)


# Date and time module

import datetime

today = datetime.datetime.now()

print(today)


# Statistics module

import statistics

numbers = [10, 20, 30, 40, 50]

print(statistics.mean(numbers))       # Mean
print(statistics.median(numbers))     # Median

# Using your own module

import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))


# Using a specific function from your own module

from calculator import add

print(add(20, 10))


# Using multiple functions from your own module

from calculator import add, subtract

print(add(30, 10))
print(subtract(30, 10))