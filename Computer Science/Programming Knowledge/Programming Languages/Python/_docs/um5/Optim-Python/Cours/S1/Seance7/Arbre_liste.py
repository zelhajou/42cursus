
        
def inserer(A,x,pos):
    if pos=="r":
        A[0]=x
    elif pos=="g":
        A[1]=[x,None,None]
    else:
        A[2]=[x,None,None]
        
def niveau(A,n):
    if A!=None:
        if n==0:
            print(A[0],end=" ")
        else:
            niveau(A[1],n-1)
            niveau(A[2],n-1)
def inordre(A):
    if A!=None:
        inordre(A[1])
        print(A[0])
        inordre(A[2])
def preordre(A):
    if A!=None:
        print(A[0])
        preordre(A[1]) 
        preordre(A[2])
def postordre(A):
    if A!=None:
        postordre(A[1]) 
        postordre(A[2])
        print(A[0])
        
def nombreDeNoeudsParNiveau (A,n):
    if A!=None:
        if n==0:return 1
        else:
            return nombreDeNoeudsParNiveau (A[1],n-1)+\
                   nombreDeNoeudsParNiveau (A[2],n-1)
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
        if A[0]==x:return True
        else:return chercher(x,A[1]) or chercher(x,A[2])
    else:return False
        
def listeDenoeudsParNiveau(A,n):
    if A!=None:
        if n==0:return [A[0]]
        else:return listeDenoeudsParNiveau(A[1],n-1)+listeDenoeudsParNiveau(A[2],n-1)
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
    else:return listInordre(A[1])+[A[0]]+listInordre(A[2])

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
        transformerListe(L,A[1],2*i+1)
    if 2*i+2<len(L):
        inserer(A,L[2*i+2],"d")
        transformerListe(L,A[2],2*i+2)
        
def transformerArbre(A) :
    return listInordre(A)


    
A=[None,None,None]
inserer(A,1,"r")
inserer(A,2,"g")
inserer(A,3,"d")


inserer(A[1],4,"g")
inserer(A[1],5,"d")

inserer(A[2],6,"g")
inserer(A[2],7,"d")

inserer(A[1][1],8,"g")
inserer(A[1][1],9,"d")

inserer(A[1][1][1],0,"g")




