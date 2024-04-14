
from scipy.optimize import bisect,fsolve,newton
def f(x):
    return x**2-x-1

f(-4)
19
f(0)
-1
bisect(f,-4,0)
-0.6180339887487207
f(-0.6180339887487207)
-2.62545540863357e-12
f(4)
11
f(10)
89
bisect(f,4,10)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    bisect(f,4,10)
  File "C:\Logiciel\Winpython64-3.10.0.1b2\WPy64-31001b2\python-3.10.0b4.amd64\lib\site-packages\scipy\optimize\zeros.py", line 549, in bisect
    r = _zeros._bisect(f, a, b, xtol, rtol, maxiter, args, full_output, disp)
ValueError: f(a) and f(b) must have different signs
fsolve(f,-4)
array([-0.61803399])
newton(f,-4)
-0.6180339887498949
fsolve(f,4)
array([1.61803399])
newton(f,4)
1.6180339887498951
bisect(f,0,4)
1.6180339887487207
from sympy import var,solve
var("x")
x
solve(f(x))
[1/2 - sqrt(5)/2, 1/2 + sqrt(5)/2]
def g(x):return x**2+2*x+1

solve(g(x))
[-1]
fsolve(g,5)
array([-1.])
newton(g,5)
-0.9999999781091519
bisect(g,-7,10)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    bisect(g,-7,10)
  File "C:\Logiciel\Winpython64-3.10.0.1b2\WPy64-31001b2\python-3.10.0b4.amd64\lib\site-packages\scipy\optimize\zeros.py", line 549, in bisect
    r = _zeros._bisect(f, a, b, xtol, rtol, maxiter, args, full_output, disp)
ValueError: f(a) and f(b) must have different signs
