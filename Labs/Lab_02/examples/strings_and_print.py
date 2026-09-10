"""
Lecture 02 Example — Strings and print()
"""

first_name = "Anna"
last_name = "Smith"

full_name = first_name + " " + last_name

print(full_name)
print(len(full_name))
print(full_name[0])
print(full_name[-1])
print(full_name[:3])

print("Python" * 3)

name = "Anna"
age = 22

print(name, age)
print(name, age, sep=" | ")

print("Python", end=" ")
print("Programming")