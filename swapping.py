# Swapping of Variables in Python

# Swapping using Python's multiple assignment

a = 10
b = 20

a, b = b, a

print(a)
print(b)


# Swapping using a temporary variable

a = 10
b = 20

temp = a
a = b
b = temp

print(a)
print(b)


# Swapping using + and -

a = 10
b = 20

a = a + b
b = a - b
a = a - b

print(a)
print(b)


# Swapping using - and +

a = 10
b = 20

a = a - b
b = a + b
a = b - a

print(a)
print(b)


# Swapping multiple variables

a = 10
b = 20
c = 30

a, b, c = c, a, b

print(a)
print(b)
print(c)


# Swapping string variables

first_name = "Chitra"
last_name = "Shrestha"

first_name, last_name = last_name, first_name

print(first_name)
print(last_name)


# Other example

x = 50
y = 100

x, y = y, x

print("x =", x)
print("y =", y)