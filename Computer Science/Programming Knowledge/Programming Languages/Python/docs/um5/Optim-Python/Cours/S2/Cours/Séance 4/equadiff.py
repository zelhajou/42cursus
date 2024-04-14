from pylab import linspace,plot,show,legend
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

a,b,n=0,5,50
y0=1
def f(y,t):
    return y

t=linspace(a,b,n)
y_od=odeint(f,y0,t)
plot(t,y_od,label="odeint")

y_el=euler_expl(f,a,b,y0,n)
plot(t,y_el,label="euler_expl")

y_elImpl=euler_impl(f,a,b,y0,n)
plot(t,y_elImpl,label="euler_impl")

y_elModif=euler_modif(f,a,b,y0,n)
plot(t,y_elModif,label="euler_modif")

y_heun=heun(f,a,b,y0,n)
plot(t,y_heun,label="heun")

y_RK4=RK4(f,a,b,y0,n)
plot(t,y_RK4,label="RK4")


legend()

show()
