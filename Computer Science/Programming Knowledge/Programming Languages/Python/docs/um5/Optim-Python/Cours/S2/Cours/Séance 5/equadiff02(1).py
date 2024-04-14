from pylab import linspace,plot,show,legend,subplot,title
from scipy.integrate import odeint

def euler_expl(f,a,b,y0,n):
    t=[a]*n  #t=[t0,t0,t0,...,t0]
    y=[y0]*n  #y=[y0,y0,...,y0]
    h=(b-a)/n
    for i in range(0,n-1,1):
        y[i+1]=y[i]+h*f(y[i],t[i])
        t[i+1]=t[i]+h
    return y

def euler_impl(f,a,b,y0,n):
    t=[a]*n  #t=[t0,t0,t0,...,t0]
    y=[y0]*n  #y=[y0,y0,...,y0]
    h=(b-a)/n
    for i in range(0,n-1,1):
        k=y[i]+h*f(y[i],t[i])
        y[i+1]=y[i]+h*f(k,t[i]+h)
        t[i+1]=t[i]+h
    return y
def euler_modif(f,a,b,y0,n):
    t=[a]*n  #t=[t0,t0,t0,...,t0]
    y=[y0]*n  #y=[y0,y0,...,y0]
    h=(b-a)/n
    for i in range(0,n-1,1):
        tm=t[i]+h/2
        ym=y[i]+h/2*f(y[i],t[i])
        y[i+1]=y[i]+h*f(ym,tm)
        t[i+1]=t[i]+h
    return y
def heun(f,a,b,y0,n):
    t=[a]*n  #t=[t0,t0,t0,...,t0]
    y=[y0]*n  #y=[y0,y0,...,y0]
    h=(b-a)/n
    for i in range(0,n-1,1):
        k=y[i]+h*f(y[i],t[i])
        y[i+1]=y[i]+h/2*(f(y[i],t[i])+f(k,t[i]+h))
        t[i+1]=t[i]+h
    return y
def RK4(f,a,b,y0,n):
    t=[a]*n  #t=[t0,t0,t0,...,t0]
    y=[y0]*n  #y=[y0,y0,...,y0]
    h=(b-a)/n
    for i in range(0,n-1,1):
        k=y[i]+h*f(y[i],t[i])
        ym=y[i]+h/2*f(y[i],t[i])
        tm=t[i]+h/2
        y[i+1]=y[i]+h/6*(f(y[i],t[i])+4*f(ym,tm)+f(k,t[i]+h))
        t[i+1]=t[i]+h
    return y

def Nystrom(f,a,b,y0,n):
    t=[a]*n  #t=[t0,t0,t0,...,t0]
    y=[y0]*n  #y=[y0,y0,...,y0]
    h=(b-a)/n
    y[1]=y[0]+h*f(y[0],t[0])
    for i in range(1,n-1,1):
        y[i+1]=y[i-1]+2*h*f(y[i],t[i])
        t[i+1]=t[i]+h
    return y




a,b,n=0,5,50
y0=1
def f(y,t):
    return y

t=linspace(a,b,n)
y_od=odeint(f,y0,t)
subplot(4,2,1)
title("odeint")
plot(t,y_od,label="odeint")

y_el=euler_expl(f,a,b,y0,n)
subplot(4,2,2)
title("euler_expl")
plot(t,y_el,label="euler_expl")

y_elImpl=euler_impl(f,a,b,y0,n)
subplot(4,2,3)
title("euler_impl")
plot(t,y_elImpl,label="euler_impl")

y_elModif=euler_modif(f,a,b,y0,n)
subplot(4,2,4)
title("euler_modif")
plot(t,y_elModif,label="euler_modif")

y_heun=heun(f,a,b,y0,n)
subplot(4,2,5)
title("heun")
plot(t,y_heun,label="heun")

y_RK4=RK4(f,a,b,y0,n)
subplot(4,2,6)
title("RK4")
plot(t,y_RK4,label="RK4")

y_Nys=Nystrom(f,a,b,y0,n)
subplot(4,2,7)
title("Nystrom")
plot(t,y_Nys)


show()
