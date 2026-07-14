# Program to swap two numbers without using a third variable

# 1. Take input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# 2. Show values before swap
print("Before swap: a =", a, "b =", b)

# 3. Swap logic (tuple unpacking)
a, b = b, a

# 4. Show values after swap
print("After swap:  a =", a, "b =", b)