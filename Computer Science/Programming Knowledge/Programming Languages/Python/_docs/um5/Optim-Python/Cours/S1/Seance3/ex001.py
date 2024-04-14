
===== RESTART:  ex01.py ====
>>> 
===== RESTART:  ex01.py ====
>>> L=[4,2,1,5,8,9,0,1,3]
>>> triInsertion(L)
>>> L
[0, 1, 1, 2, 3, 4, 5, 8, 9]
>>> a=10
>>> b=10
>>> a,b=b=a
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a,b=b=a
TypeError: cannot unpack non-iterable int object
>>> a,b=b,a
>>> a
10
>>> b
10
>>> 
===== RESTART:  ex01.py ====
>>> L=[4,2,1,5,8,9,0,1,3]
>>> triSelection(L)
>>> L
[0, 1, 1, 2, 3, 4, 5, 8, 9]
>>> 
===== RESTART:  ex01.py ====
>>> L1=[1,2,5,9,10]
>>> L2=[3,7,10,20,30,40]
>>> fusion(L1,L2)
[1, 2, 3, 5, 7, 9, 10, 10, 20, 30, 40]
>>> 
===== RESTART:  ex01.py ====
>>> L=[4,2,1,5,8,9,0,1,3]
>>> triFusion(L)
[0, 1, 1, 2, 3, 4, 5, 8, 9]
>>> 
===== RESTART:  ex01.py ====
>>> 
===== RESTART:  ex01.py ====
>>> L1=[1,2,5,9,10]
>>> L=[4,2,1,5,8,9,0,1,3]
>>> triRapide(L)
[0, 1, 1, 2, 3, 4, 5, 8, 9]
>>> #La creation
>>> T=(1,4,5,8,7,9,6,5,3)
>>> type(T)
<class 'tuple'>
>>> T1=(4,2,4,2,5,10.8,5+8j,"Ali",(1,4),[4,0,8],"A")
>>> type(T1)
<class 'tuple'>
>>> T2=4,5,8,9,1
>>> T2
(4, 5, 8, 9, 1)
>>> len(T2)
5
>>> T3=4,5,(8,9),1
>>> T3
(4, 5, (8, 9), 1)
>>> len(T3)
4
>>> a,b=10,5
>>> (a,b)=(10,5)
>>> a
10
>>> b
5
>>> (a,b)=(b,a)
>>> a
5
>>> b
10
>>> x=10
>>> type(x)
<class 'int'>
>>> x=(10)
>>> type(x)
<class 'int'>
>>> x=(10,)
>>> type(x)
<class 'tuple'>
>>> len(x)
1
>>> x=()
>>> type(x)
<class 'tuple'>
>>> len(x)
0
>>> x=(,10)
SyntaxError: invalid syntax
>>> #L'accès
>>> T
(1, 4, 5, 8, 7, 9, 6, 5, 3)
>>> T[0]
1
>>> T[-1]
3
>>> T[0:5]
(1, 4, 5, 8, 7)
>>> T[0::2]
(1, 5, 7, 6, 3)
>>> #La modification
>>> T
(1, 4, 5, 8, 7, 9, 6, 5, 3)
>>> T[0]=40
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    T[0]=40
TypeError: 'tuple' object does not support item assignment
>>> T=list(T)
>>> T
[1, 4, 5, 8, 7, 9, 6, 5, 3]
>>> T[0]=40
>>> T
[40, 4, 5, 8, 7, 9, 6, 5, 3]
>>> T=tuole(T)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    T=tuole(T)
NameError: name 'tuole' is not defined
>>> T=tuple(T)
>>> T
(40, 4, 5, 8, 7, 9, 6, 5, 3)
>>> T
(40, 4, 5, 8, 7, 9, 6, 5, 3)
>>> id(T)
48802608
>>> T=list(T)
>>> T[0]=100
>>> T=tuple(T)
>>> T
(100, 4, 5, 8, 7, 9, 6, 5, 3)
>>> id(T)
48802608
>>> T=list(T)
>>> T[0]=4000
>>> T=tuple(T)
>>> T
(4000, 4, 5, 8, 7, 9, 6, 5, 3)
>>> id(T)
48802608
>>> 
==================================== RESTART: Shell ===================================
>>> T=(100, 4, 5, 8, 7, 9, 6, 5, 3)
>>> id(T)
48806704
>>> T=list(T)
>>> T[4]=500
>>> T
[100, 4, 5, 8, 500, 9, 6, 5, 3]
>>> T=tuple(T)
>>> T
(100, 4, 5, 8, 500, 9, 6, 5, 3)
>>> id(T)
48806704
>>> T=list(T)
>>> T
[100, 4, 5, 8, 500, 9, 6, 5, 3]
>>> id(T)
49435520
>>> T=(100, 4, 5, 8, 7, 9, 6, 5, 3)
>>> id(T)
48806704
>>> T=list(T)
>>> id(T)
49436544
>>> T[0]=600
>>> T
[600, 4, 5, 8, 7, 9, 6, 5, 3]
>>> #La recherche
>>> T
[600, 4, 5, 8, 7, 9, 6, 5, 3]
>>> T=(4,7,8,9)
>>> T[0]=500
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    T[0]=500
TypeError: 'tuple' object does not support item assignment
>>> id(T)
48855936
>>> T=list(T)
>>> id(T)
49435520
>>> A=(4,7,8,9,10,20)
>>> id(A)
49503968
>>> T=list(T)
>>> T[0]=500
>>> T=(4,7,8,9)
>>> id(T)
49303120
>>> A=(7,5,9,0)
>>> id(A)
49374128
>>> T[0]=500
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    T[0]=500
TypeError: 'tuple' object does not support item assignment
>>> T=list(T)
>>> id(T)
49345344
>>> T[0]=500
>>> T
[500, 7, 8, 9]
>>> id(T)
49345344
>>> T=tuple(T)
>>> id(T)
49449456
>>> x=200
>>> id(x)
8790881525632
>>> x=500
>>> id(x)
49253840
>>> #La recherche
>>> T
(500, 7, 8, 9)
>>> 50 in T
False
>>> 7 in T
True
>>> (7,8) in T
False
>>> T=(500, (7, 8), 9)
>>> (7,8) in T
True
>>> #Les operations
>>> (10,20)*5
(10, 20, 10, 20, 10, 20, 10, 20, 10, 20)
>>> (10,20)+(20,30,40)
(10, 20, 20, 30, 40)
>>> 10,20+20,30,40
(10, 40, 30, 40)
>>> T
(500, (7, 8), 9)
>>> T=(4,5,8,9,7,4)
>>> T
(4, 5, 8, 9, 7, 4)
>>> T
(4, 5, 8, 9, 7, 4)
>>> id(T)
49503968
>>> T=T[:2]+(100,)+T[3:]
>>> T
(4, 5, 100, 9, 7, 4)
>>> id(T)
49218368
>>> T
(4, 5, 100, 9, 7, 4)
>>> max(T)
100
>>> len(L)
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    len(L)
NameError: name 'L' is not defined
>>> len(T)
6
>>> min(T)
4
>>> sum(T)
129
>>> #Les methodes
>>> T.index(100)
2
>>> T.count(100)
1
>>> L=[1,2,5]
>>> 
