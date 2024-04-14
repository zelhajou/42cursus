from pylab import *
from scipy.integrate import odeint

def f(z,t):
    return array((z[1],-E0*w**2*sin(w*t)-R/L*z[1]-1/(L*C)*z[0]))


a,b,n=0,0.3,150
R,L,C,E0=20,0.8,700*10**(-6),10
freq=80
vb=0
dvb=0
w=2*pi*freq
z0=array((vb,dvb))
t=linspace(a,b,n)
z=odeint(f,z0,t)
UL=[e[0] for e in z]
ULp=[e[1] for e in z]
subplot(2,1,1)
title("UL(t)")
plot(t,UL)
subplot(2,1,2)
title("ULp(t)")
plot(t,ULp)

show()



