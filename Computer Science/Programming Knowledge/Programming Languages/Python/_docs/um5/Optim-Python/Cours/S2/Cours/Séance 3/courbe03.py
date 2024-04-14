#les courbes
from pylab import *

(a,b,n)=(0,10,100)

xi=linspace(a,b,n)
yi=cos(xi)
plot(xi,yi,"bv")


title("La fonction cos ")
xlabel("Axes des XI")
ylabel("Axes des YI")


show()
