"""
Write a program that asks the user for a sentence and:

1. Converts it to lowercase.
2. Counts the number of vowels (a, e, i, o, u).
"""
sentence =  input("Type your sentence: ").lower()
vowels = "aeiou"
count = 0
for x in sentence:
    if x in vowels:
        count +=1
print(count)