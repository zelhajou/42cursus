
>>> x=10
>>> type(x)
<class 'int'>
>>> x=10.5
>>> type(x)
<class 'float'>
>>> x=14+15j
>>> type(x)
<class 'complex'>
>>> 10+3
13
>>> 10*3
30
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> 10**3
1000
>>> 10%3
1
>>> 10<3
False
>>> 10<=3
False
>>> 10=<3
SyntaxError: invalid syntax
>>> 10!=3
True
>>> 10=!3
SyntaxError: invalid syntax
>>> 10==3
False
>>> 10<3 and 12>5
False
>>> not 10<3
True
>>> 10<3 or 12>5
True
>>> 10<3 Or 12>5
SyntaxError: invalid syntax
>>> x=10
>>> x+=3
>>> x
13
>>> x*=10
>>> x
130
>>> x//=10
>>> x
13
>>> x=*5
SyntaxError: can't use starred expression here
>>> x=+6
>>> x
6
>>> 10**3
1000
>>> 4**0.
1.0
>>> 4**0.5
2.0
>>> x
6
>>> x++
SyntaxError: invalid syntax
>>> x+=1
>>> x
7
>>> x-=1
>>> x
6
>>> x
6
>>> x--
SyntaxError: invalid syntax
>>> 10/5*2
4.0
>>> 10/(5*2)
1.0
>>> 10<5+9
True
>>> 10<(5+9)
True
>>> x=10<5+9
>>> x
True
>>> abs(-4)
4
>>> max(1,4,8,7,1,5)
8
>>> min(1,4,8,7,1,5)
1
>>> sqrt(4)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    sqrt(4)
NameError: name 'sqrt' is not defined
>>> from math import *
>>> sqrt(4)
2.0
>>> pi
3.141592653589793
>>> e
2.718281828459045
>>> cos(4)
-0.6536436208636119
>>> exp(1)
2.718281828459045
>>> linspace(1,10,5)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    linspace(1,10,5)
NameError: name 'linspace' is not defined
>>> from numpy import *
>>> linspace(1,10,5)
array([ 1.  ,  3.25,  5.5 ,  7.75, 10.  ])
>>> from numpy.random import *
>>> from numpy.linalg import *
>>> A=randint(2,9,(4,4))
>>> A
array([[7, 7, 4, 5],
       [3, 6, 8, 3],
       [4, 8, 6, 3],
       [4, 4, 3, 4]])
>>> det(A)
-97.00000000000009
>>> transpose(A)
array([[7, 3, 4, 4],
       [7, 6, 8, 4],
       [4, 8, 6, 3],
       [5, 3, 3, 4]])
>>> inv(A)
array([[ 0.72164948,  0.25773196, -0.44329897, -0.7628866 ],
       [-0.2371134 , -0.29896907,  0.4742268 ,  0.16494845],
       [ 0.12371134,  0.32989691, -0.24742268, -0.21649485],
       [-0.57731959, -0.20618557,  0.15463918,  1.01030928]])
>>> f(10)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    f(10)
  File "mtrand.pyx", line 1494, in numpy.random.mtrand.RandomState.f
TypeError: f() takes at least 2 positional arguments (1 given)
>>> 
======================================== RESTART: Shell =======================================
>>> f(10)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    f(10)
NameError: name 'f' is not defined
>>> def f(x):
	return x**2

>>> f(10)
100
>>> f(5)
25
>>> g=lambda x:x**2
>>> g(5)
25
>>> g(4)
16
>>> def affichage(x,y):
	print(x+y)
	print(x*y)
	print(x/y)

	
>>> affichage(10,5)
15
50
2.0
>>> def affichage(x,y):
	print(x+y)
	 print(x*y)
	print(x/y)
	
SyntaxError: unexpected indent
>>> bin(12)
'0b1100'
>>> oct(12)
'0o14'
>>> hex(123)
'0x7b'
>>> int(0b1100)
12
>>> int(0o14)
12
>>> int(0x7b)
123
>>> int(0o14)
12
>>> oct(12)
'0o14'
>>> bin(0o146)
'0b1100110'
>>> bin(0x146)
'0b101000110'
>>> oct(0b1100110)
'0o146'
>>> hex(0b11000110)
'0xc6'
>>> oct(0xc6)
'0o306'
>>> hex(0o306)
'0xc6'
>>> from math import *
>>> ceil(4.8)
5
>>> ceil(4.3)
5
>>> floor(4.8)
4
>>> floor(4.3)
4
>>> round(4.8)
5
>>> round(4.3)
4
>>> round(4.5)
4
>>> round(7.5)
8
>>> def unite(n):
	return n%10

>>> unite(153)
3
>>> unite(45879)
9
>>> def coef(n,i):
	return unite(n/(10**i))

>>> coef(153,0)
3.0
>>> def coef(n,i):
	return unite(n//(10**i))

>>> coef(153,0)
3
>>> coef(153,1)
5
>>> coef(153,2)
1
>>> coef(153,3)
0
>>> coef(153,9)
0
>>> coef(48795462157153,9)
5
>>> def solve(a,b):
	if a!=0:
		s=-b/a
	if a==0 and b==0:
		x="R"
	if a==0 and b!=0:
		x="vid"
	return x

>>> solve(2,6)
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    solve(2,6)
  File "<pyshell#136>", line 8, in solve
    return x
UnboundLocalError: local variable 'x' referenced before assignment
>>> def solve(a,b):
	if a!=0:
		x=-b/a
	if a==0 and b==0:
		x="R"
	if a==0 and b!=0:
		x="vid"
	return x

>>> solve(2,6)
-3.0
>>> solve(0,6)
'vid'
>>> solve(0,0)
'R'
>>> def solve02(a,b):
	if a!=0:
		x=-b/a
	else:
		if b==0:
			x="R"
		else:
			x="vid"
	return x

>>> solve02(2,6)
-3.0
>>> solve02(0,6)
'vid'
>>> solve02(0,0)
'R'
>>> def solve03(a,b):
	if a!=0:
		x=-b/a
	elif b==0:
		x="R"
	else:
		x="vid"
	return x

>>> solve03(2,6)
-3.0
>>> solve03(0,6)
'vid'
>>> solve03(0,0)
'R'
>>> def somme(n):
	if n==0:
		return 0
	else:
		return n+somme(n-1)

	
>>> 0+1+2+3+4
10
>>> somme(4)
10
>>> def ommech(n):
	if n<10:
		return n
	else:
		return n%10+sommech(n//10)

	
>>> sommech(153)
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    sommech(153)
NameError: name 'sommech' is not defined
>>> def sommech(n):
	if n<10:
		return n
	else:
		return n%10+sommech(n//10)

	
>>> sommech(153)
9
>>> ~10
-11
>>> 10&12
8
>>> 10|12
14
>>> 
