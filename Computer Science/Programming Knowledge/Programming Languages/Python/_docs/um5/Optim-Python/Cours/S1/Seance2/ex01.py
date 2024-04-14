def somme(n):
    s=0
    i=0
    while i<n:
        i+=1
        s+=i
    return s
def ppcm(a,b):
    x=a
    y=b
    while x!=y:
        if x<y:
            x+=a
        else:
            y+=b
    return x
def amstrang(n):
    s=0
    N=n
    while n!=0:
        s+=(n%10)**3
        n//=10
    return s==N

def pgcd(a,b):
    m=min(a,b)
    seq=range(1,m+1,1)
    for i in seq:
        if a%i==0 and b%i==0:
            d=i
    return d
def pgcdM2(a,b):
    m=min(a,b)
    seq=range(m,0,-1)
    for i in seq:
        if a%i==0 and b%i==0:
            d=i
            break
    return d
def constE(n=500):
    s=0
    seq=range(0,n+1,1)
    for i in seq:
        s+=1/fact(i)
    return s
def fact(n):
    f=1
    seq=range(2,n+1)
    for i in seq:
        f*=i
    return f

def triBull(L):
    n=len(L)
    for j in range(n-1,0,-1):
        for i in range(0,j,1):
            if L[i]>L[i+1]:
                L[i],L[i+1]=L[i+1],L[i]
                #x=L[i]
                #L[i]=L[i+1]
                #L[i+1]=x
    
                
                

