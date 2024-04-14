from pylab import *
from scipy.integrate import odeint

def f(z,t):
    y=z[0]
    yp=z[1]
    return array((yp,-0.2*yp-y+2*cos(3*t)))


a,b,n=0,5,50
z0=array((1,0))
t=linspace(a,b,n)
z=odeint(f,z0,t)
y=[e[0] for e in z]
yp=[e[1] for e in z]
plot(t,y,label="y(t)")
plot(t,yp,label="yp(t)")
legend()
show()
