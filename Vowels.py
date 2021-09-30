"""

You need to make a program that counts the number of vowels in a given text.
The vowels are a, e, i, o, and u.

Take a string as input and output the number of vowels
"""

txt = input()
vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
count = 0
for i in range(0, len(txt)):
    if txt[i] in vowel:
        count += 1
print(count)
