"""
x=? f(x)=0
from scipy.optimize import bisect,newton,fsolve
1)bisect
2)fsolve
3)newton
from sumpy import var,solve
4)solve

5)dichotomie
6)lagrange
7)newton
8)sécante
"""
def dichotomieI(f,a,b,eps=10**(-10)):
    while abs(b-a)>eps:
        x=(a+b)/2
        if f(x)*f(b)<=0:
            a=x
        else:
            b=x
    return (a+b)/2

def dichotomieR(f,a,b,eps=10**(-10)):
    if abs(b-a)>eps:
        x=(a+b)/2
        if f(x)*f(b)<=0:
            return dichotomieR(f,x,b)
        else:
            return dichotomieR(f,a,x)
    else:
        return (a+b)/2

def lagrangeI(f,a,b,eps=10**(-10)):
    x=(a*f(b)-b*f(a))/(f(b)-f(a))
    while abs(f(x))>eps:
        if f(x)*f(b)<=0:
            a=x
        else:
            b=x
        x=(a*f(b)-b*f(a))/(f(b)-f(a))
    return x
              
def lagrangeR(f,a,b,eps=10**(-10)):
    x=(a*f(b)-b*f(a))/(f(b)-f(a))
    if abs(f(x))>eps:
        if f(x)*f(b)<=0:
            a=x
        else:
            b=x
        return lagrangeR(f,a,b)
    else:
        return x

def newtonI(f,x0,h=0.001,eps=10**(-10)):
    while abs(f(x0))>eps:
        x=x0-(f(x0)*2*h)/(f(x0+h)-f(x0-h))
        x0=x
    return x0
def newtonR(f,x0,h=0.001,eps=10**(-10)):
    if abs(f(x0))>eps:
        x=x0-(f(x0)*2*h)/(f(x0+h)-f(x0-h))
        return newtonR(f,x)
    else:
        return x0

def secanteI(f,xi,xj,eps=10**(-10)):
    while abs(xj-xi)>eps:
        x=(xi*f(xj)-xj*f(xi))/(f(xj)-f(xi))
        xi,xj=x,xi
    return xi

def secanteR(f,xi,xj,eps=10**(-10)):
    if abs(xj-xi)>eps:
        x=(xi*f(xj)-xj*f(xi))/(f(xj)-f(xi))
        return secanteR(f,x,xi)
    else:
        return xi



        







