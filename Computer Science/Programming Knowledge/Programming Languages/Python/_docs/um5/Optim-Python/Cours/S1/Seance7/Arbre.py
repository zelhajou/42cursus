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
        
def nombreDeNoeudsParNiveau (A,n):
    if A!=None:
        if n==0:return 1
        else:
            return nombreDeNoeudsParNiveau (A.g,n-1)+\
                   nombreDeNoeudsParNiveau (A.d,n-1)
    else:return 0
def nombreDeNiveaux (A):
    i=0
    while nombreDeNoeudsParNiveau(A,i)!=0:
        i+=1
    return i
        
def nombreDeNoeuds(A):
    s=0
    n=nombreDeNiveaux(A)
    for i in range(n):
        s+=nombreDeNoeudsParNiveau(A,i)
    return s
def affichageEnLargeur(A):
    n=nombreDeNiveaux(A)
    for i in range(n):
        niveau(A,i)
def chercher(x,A):
    if A!=None:
        if A.racine==x:return True
        else:return chercher(x,A.g) or chercher(x,A.d)
    else:return False
        
def listeDenoeudsParNiveau(A,n):
    if A!=None:
        if n==0:return [A.racine]
        else:return listeDenoeudsParNiveau(A.g,n-1)+listeDenoeudsParNiveau(A.d,n-1)
    else:return [None]
def parfaitComplet(A):
    n=nombreDeNiveaux(A)
    for i in range(n):
        if nombreDeNoeudsParNiveau(A,i)!=2**i:
            return False
    return True
def parfait(A):
    n=nombreDeNiveaux(A)
    for i in range(n-1):
        if nombreDeNoeudsParNiveau(A,i)!=2**i:
            return False
    L=listeDenoeudsParNiveau(A,n-1)
    if None in L:
        j=L.index(None)
        return L[j:]==[None]*(len(L)-j)
    else:return True
def listInordre(A):
    if A==None:return []
    else:return listInordre(A.g)+[A.racine]+listInordre(A.d)

def arbreDerecherche(A):  #g<=p<=d
    L=listInordre(A)
    L1=L.copy()
    L1.sort()
    return L==L1
def transformerListe(L,A,i=0):
    if i==0:
        inserer(A,L[i],"r")
    if 2*i+1<len(L):
        inserer(A,L[2*i+1],"g")
        transformerListe(L,A.g,2*i+1)
    if 2*i+2<len(L):
        inserer(A,L[2*i+2],"d")
        transformerListe(L,A.d,2*i+2)
        
def transformerArbre(A) :
    return listInordre(A)


    
A=Arbre()
inserer(A,1,"r")
inserer(A,2,"g")
inserer(A,3,"d")


inserer(A.g,4,"g")
inserer(A.g,5,"d")

inserer(A.d,6,"g")
inserer(A.d,7,"d")

#inserer(A.g.g,8,"g")
#inserer(A.g.g,9,"d")

#inserer(A.g.g.g,0,"g")




