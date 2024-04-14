def gauche ( i ) :
    return 2*i+1

def droite(i) :
    return 2*i+2

def pere(i):
    return (i-1)//2

def maximum(T,i,limite):
    #T[i],T[g],T[d]
    imax=i
    if gauche(i)<limite and T[imax]<T[gauche(i)]:
        imax=gauche(i)
    if droite(i)<limite and T[imax]<T[droite(i)]:
        imax=droite(i)
    return imax
def entasser(T,i,limite ):
    imax=maximum(T,i,limite)
    if i!=imax:
        T[i],T[imax]=T[imax],T[i]
        entasser(T,imax,limite )
def construireTas(T):
    n=len(T)
    for i in range(n-1,-1,-1):
        entasser(T,i,n)
def estunTas(T) :
    for i in range(1,len(T)):
        if T[i]>T[pere(i)]:
            return False
    return True
def trierTas(T):
    n=len(T)
    for i in range(n-1,0,-1):
        T[0],T[i]=T[i],T[0]
        entasser(T,0,i)
       
def triParTas(T ):
    if estunTas(T)==False:
        construireTas(T)
    trierTas(T)
    






        

