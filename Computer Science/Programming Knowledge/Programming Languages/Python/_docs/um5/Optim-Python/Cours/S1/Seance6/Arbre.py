class Arbre:
    def __init__(A,racine=None,pg=None,pd=None):
        A.racine=racine
        A.g=pg
        A.d=pd
        
def inserer(A,x,pos):
    if pos=="r":
        A.racine=x
    elif pos=="g":
        A.g=Arbre(x)
    else:
        A.d=Arbre(x)
        
def niveau(A,n):
    if A!=None:
        if n==0:
            print(A.racine,end=" ")
        else:
            niveau(A.g,n-1)
            niveau(A.d,n-1)
def inordre(A):
    if A!=None:
        inordre(A.g)
        print(A.racine)
        inordre(A.d)
def preordre(A):
    if A!=None:
        print(A.racine)
        preordre(A.g) 
        preordre(A.d)
            
def postordre(A):
    if A!=None:
        postordre(A.g) 
        postordre(A.d)
        print(A.racine)


    
A=Arbre()
inserer(A,["Mohamed",15],"r")
inserer(A,["Ali",14],"g")
inserer(A,["Sara",19],"d")


inserer(A.g,4,"g")
inserer(A.g,5,"d")

inserer(A.d,6,"g")
inserer(A.d,7,"d")

inserer(A.g.g,8,"g")
inserer(A.g.g,9,"d")

inserer(A.g.g.g,0,"g")




