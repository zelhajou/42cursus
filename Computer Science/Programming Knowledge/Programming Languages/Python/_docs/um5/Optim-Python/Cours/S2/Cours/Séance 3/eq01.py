
from pylab import *
from scipy.integrate import odeint

def f(y,t):
    return y
 
a,b,n=0,5,50
y0=1
t=linspace(a,b,n)
y=odeint(f,y0,t)
plot(t,y)
show()
