def triInsertion(L):
    n=len(L)
    for i in range(0,n-1,1):
        inserer(L,i+1,L[i+1])

def inserer(L,n,x):
    j=n-1
    while j>=0 and L[j]>x:
        L[j+1]=L[j]
        j-=1
    L[j+1]=x
    
def triSelection(L):
    n=len(L)
    for i in range(n):
        j=getIndex(L,i,n-1)
        if i!=j:
            L[i],L[j]=L[j],L[i]
def getIndex(L,a,b):
    j=a
    for k in range(a+1,b+1):
        if L[k]<L[j]:
            j=k
    return j
def fusion(L1,L2):
    if L1==[]:
        return L2
    elif L2==[]:
        return L1
    elif L1[0]<L2[0]:
        return [L1[0]]+fusion(L1[1:],L2)
    else:
        return [L2[0]]+fusion(L1,L2[1:])
def triFusion(L):
    if len(L)<=1:
        return L
    else:
        L1=triFusion(L[:len(L)//2])
        L2=triFusion(L[len(L)//2:])
        return fusion(L1,L2)
from numpy.random import randint
def triRapide(L):
    if len(L)<=1:
        return L
    else:
        i=randint(0,len(L)-1)
        Pivot=L.pop(i)
        L1=[]
        L2=[]
        for x in L:
            if x<Pivot:
                L1.append(x)
            else:
                L2.append(x)
        return triRapide(L1)+[Pivot]+triRapide(L2)
    
        

    
