#les courbes
from pylab import *

(a,b,n)=(0,10,100)

xi=linspace(a,b,n)
yi=cos(xi)
subplot(221)
plot(xi,yi)
title("La fonction cos")
xlabel("Axes des XI")
ylabel("Axes des YI")

zi=sin(xi)
subplot(2,2,2)
plot(xi,zi)

title("La fonction sin")
xlabel("Axes des XI")
ylabel("Axes des YI")


zi=tan(xi)
subplot(2,2,3)
plot(xi,zi)

title("La fonction tan")
xlabel("Axes des XI")
ylabel("Axes des YI")

def f(x):
    return x**2

xi=linspace(-10,10,500)
zi=f(xi)
subplot(2,2,4)
plot(xi,zi)

title("La fonction x**2")
xlabel("Axes des XI")
ylabel("Axes des YI")



show()
