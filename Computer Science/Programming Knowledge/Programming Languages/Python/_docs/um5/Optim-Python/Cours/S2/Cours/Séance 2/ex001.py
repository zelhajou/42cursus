chapitre 02  s=?/.....
1)quad
2)trapz
3)simps
4)methode des rectangles
5)methode des trapezes
6)methode des simpsons

def rectangles(f,a,b,n=50):
    s=0
    h=(b-a)/n
    for i in range(0,n,1):
        xi=a+i*h
        s+=f(xi+h/2)
    return h*s
def trapezes(f,a,b,n):
    s=0
    h=(b-a)/n
    for i in range(0,n,1):
        xi=a+i*h
        s+=f(xi)+f(xi+h)
    return (h/2)*s
def simpsons(f,a,b,n):
    s=0
    h=(b-a)/n
    for i in range(0,n,1):
        xi=a+i*h
        s+=f(xi)+4*f(xi+h/2)+f(xi+h)
    return (h/6)*s
from math import cos,sin
def f(x):
    return (x**5)*cos(x**3)*sin(x)

s=rectangles(f,0,1)
print("Methode des rectangles: ",s)

s=trapezes(f,0,1,50)
print("Methode des trapezes: ",s)

s=simpsons(f,0,1,50)
print("Methode des simpsons: ",s)





