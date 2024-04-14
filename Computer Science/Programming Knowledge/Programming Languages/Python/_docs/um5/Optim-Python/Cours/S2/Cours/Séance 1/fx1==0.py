
def f(x):
    return x**2-x-1

dichotomie(f,-4,0)
-0.6180339887214359
dichotomie(f,0,4)
1.618033988721436


def f(x):
    return x**2-x-1

lagrangeI(f,-4,0)
-0.61803398871257


def f(x):
    return x**2-x-1

newton(f,-4)
-0.6180339887499123


def f(x):
    return x**2-x-1

sacante(f,4,10)
1.618033988749895
sacante(f,-4,-3)
-0.6180339887498949
newton(f,4)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    newton(f,4)
NameError: name 'newton' is not defined. Did you mean: 'newtonI'?
newtonI(f,4)
1.618033988749895
