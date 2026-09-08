
"""
Lab 01 — Python Basics

Complete all tasks below.

Topics:
- variables
- basic data types
- input and output
- type conversion
- arithmetic operators
- basic PEP 8
"""

# ============================================================
# Task 1 — Personal Information
# ============================================================

print("Task 1 — Personal Information")

# TODO:
# Ask the user to enter their name.

name: str = input("Enter your name: ")

# TODO:
# Ask the user to enter their age.
# Remember that input() returns a string.

age: int = int(input("Enter your age: "))

# TODO:
# Print:
# Hello, <name>!
# Next year you will be <age + 1> years old.
print(f"Hello, {name}")
print(f"Next year you will be {age + 1} years old.")


print()


# ============================================================
# Task 2 — Rectangle
# ============================================================

print("Task 2 — Rectangle")

width: float = float(input("Enter the width of the rectangle: "))
height: float = float(input("Enter the height of the rectangle: "))

area: float = width * height

perimeter: float = 2 *  width + 2 * height

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

print()


# ============================================================
# Task 3 — Temperature Converter
# ============================================================

print("Task 3 — Temperature Converter")

# Formula:
# Fahrenheit = Celsius * 9 / 5 + 32

celsius: float = float(input("Enter temperature in Celsius: "))

fahrenheit: float = (9.0 * celsius) / 5.0 + 32.0

print(f"{celsius}°C is equal to {fahrenheit}°F")

print()


# ============================================================
# Task 4 — Purchase Calculator
# ============================================================

print("Task 4 — Purchase Calculator")

quantity: int = int(input("Enter the number of items: "))

price: float = float(input("Enter the price of one item: "))

# TODO:
# Calculate the total price.

total_price: float = quantity * price

# TODO:
# Apply a 10% discount.

discounted_price: float = total_price * 0.90

# TODO:
# Print both results.
print(f"Total price: {total_price}")
print(f"Discounted price (10% off): {discounted_price}")

print()


# ============================================================
# Task 5 — Arithmetic Operators
# ============================================================

print("Task 5 — Arithmetic Operators")

a: int = 17
b: int = 5

# TODO:
# Print the result of each operation:
#
# a + b
# a - b
# a * b
# a / b
# a // b
# a % b
# a ** b

print(f"a + b  = {a + b}")   # Addition
print(f"a - b  = {a - b}")   # Subtraction
print(f"a * b  = {a * b}")   # Multiplication
print(f"a / b  = {a / b}")   # True division (float)
print(f"a // b = {a // b}")  # Floor division (integer)
print(f"a % b  = {a % b}")   # Modulo (remainder)
print(f"a ** b = {a ** b}")  # Exponentiation