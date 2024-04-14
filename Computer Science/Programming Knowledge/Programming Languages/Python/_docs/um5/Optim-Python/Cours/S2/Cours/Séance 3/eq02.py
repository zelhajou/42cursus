
from pylab import *
from scipy.integrate import odeint

def f(z,t):
    return array([-B*z[0]*z[1],B*z[0]*z[1]-G*z[1],G*z[1]])

B,G= 0.5,0.1
a,b,n=0,50,1000
z0=array([0.8,0.2,0])
t=linspace(a,b,n)
zi=odeint(f,z0,t)
S=[z[0] for z in zi]
I=[z[1] for z in zi]
R=[z[2] for z in zi]
plot(t,S,label="S(t)")
plot(t,I,label="I(t)")
plot(t,R,label="R(t)")
legend()
show()
