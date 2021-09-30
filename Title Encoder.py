"""You are given a file named "books.txt" with book titles, each on a separate line.
To encode the book titles you need to take the first letters of each word in the title and combine them.
For example, for the book title "Game of Thrones" the encoded version should be "GoT"."""
file = open("/usercode/files/books.txt", "r")
count=""
for line in file:#ia fiecare linie ca si item in lista file
    books=line.split()#ia fiecare cuvant ca si item in lista books
    for ch in books:# fiecare caracter din item-urile listei books
         count+=ch[0]
    print(count)
    count=""# initializeaza cu empty string pentru a putea afisa pe urmatorul rand titlu
file.close()