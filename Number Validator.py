""" You are given a number input, and need to check if it is a valid phone number.
A valid phone number has exactly 8 digits and starts with 1, 8 or 9.
Output "Valid" if the number is valid and "Invalid", if it is not.

"""

import re
number=input()
pattern=r"^1|8|9[0-9]{7}$"#orice numar care incepe cu 1,8 sau 9
match=re.match(pattern,number)
if match and len(number)==8: # verificarea daca numarul are exact 8 digiti deoarece pot fi cazuri cu repetari de cifre
   print("Valid")
else:
    print("Invalid")
