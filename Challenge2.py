"""
Challenge
Write a program that asks for a number and prints whether it is:

Divisible by 3, 5, or both.
Use multiple if, elif, and else statements to check the conditions.
"""

num = int(input("Enter a number: "))

if num%5==0 and num%3==0:
    print(f"{num} is divisible by 3")
elif num%5 == 0:
    print(f"{num} is divisible by 5")
elif num%3==0:
    print(f"{num} is divisible by both 5 and 3")
else:
    print(f"{num} is not divisible by either 3, 5, or both")
