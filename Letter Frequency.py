""" You are making a program to analyze text.
Take the text as the first input and a letter as the second input, and output the frequency of that letter in the text as a whole percentage.

Sample Input:
hello
l

Sample Output:
40

The letter l appears 2 times in the text hello, which has 5 letters. So, the frequency would be (2/5)*100 = 40.
"""

# your code goes here
word = input()
letter = input()
count = 0
for item in word:
    char = item.split()
    for ch in char:

        if ch == letter:
            count += 1
print(int(count / len(word) * 100))