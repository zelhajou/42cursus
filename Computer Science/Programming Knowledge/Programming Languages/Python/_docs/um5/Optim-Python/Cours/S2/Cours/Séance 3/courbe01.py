#les courbes
from pylab import *

(a,b,n)=(0,10,100)

xi=linspace(a,b,n)
yi=cos(xi)
plot(xi,yi,label="cos")

zi=sin(xi)
plot(xi,zi,label="sin")

title("Les fonctions cos et sin")
xlabel("Axes des XI")
ylabel("Axes des YI")

legend(loc=2)
show()
