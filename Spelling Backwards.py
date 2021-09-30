"""Given a string as input, use recursion to output each letter of the strings in reverse order, on a new line.

Sample Input
HELLO

Sample Output
O
L
L
E
H"""
txt = input()
def spell(txt):
    n=len(txt)
    if n==0: #verificam daca s-a introdus un sire de caractere
        return 0
    else:
         print(txt[n-1]) #se afiseaza ultimul caracter
         n=n-1
         return spell(txt[0:n])

spell(txt)
