"""
Task 2: Age Group
Write a program that asks for a person's age and determines if they are a child, teenager, or adult.
"""
age = int(input("Enter your age: "))

if age <= 0:
    print("YOU ENTERED AN INVALID AGE")
elif age <13:
    print("You are a child")
elif age < 18:
    print("You are a teenager")
else:
    print("You are an adult")