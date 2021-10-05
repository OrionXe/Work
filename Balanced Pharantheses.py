class stack():
    def __init__(self):
        self.items=[]# o noua instanta items care reprezinta o lista goala
    def empty(self):
        return self.items==[]#returneaza True daca self.items este goala
    def push(self,item):
        self.items.insert(0,item)#adauga item in "stack" pe pozitia 0
    def pop(self):
        self.items.pop(0)#scoate din stack elementul de pe pozitia 0
    def __call__(self):# face posibila apelarea stivei
        return self.items

def balanced(expression):
    exp_element=stack()#initializeaza variabila cu stiva creata
    for i in expression:
        if i=='(':
           exp_element.push(i)#inroduce toate parantezele deschise in stiva
        if i==')':
           if'('in exp_element(): #verifica daca in stiva se afla o paranteza deschisa
                 exp_element.pop()#scoate ultimul element==>paranteza deschisa
           else:
                return False

    if not exp_element():#verifica daca lista este goala
         return True
    else:
         return False
print(balanced(input()))

