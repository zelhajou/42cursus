from pylab import *
from scipy.integrate import odeint

def f(z,t):
    x=z[0]
    y=z[1]
    return array((x*(A-B*y),y*(D*x-C)))

A,B,C,D=1,0.005,1.5,0.01
a,b,n=0,1000,100
z0=array((100,80))
t=linspace(a,b,n)
z=odeint(f,z0,t)
x=[e[0] for e in z]
y=[e[1] for e in z]
plot(t,x,label="x(t)")
plot(t,y,label="y(t)")
legend()
show()
