
=====   ====
>>> somme(4)

=====   ====
>>> somme(4)
10
>>> 0+1+2+3+4
10
>>> somme(5)
15
>>> 
=  
>>> ppcm(3,4)
12
>>> 
=  
>>> ppcm(3,4)
12
>>> 
=  
>>> ppcm(3,4)
12
>>> 3**3+5**3+1**3
153
>>> 123
123
>>> 3**3+2**3+1**3
36
>>> 407
407
>>> 4**3+0**3+7**3
407
>>> 
=  
>>> amstrang(153)
True
>>> amstrang(123)
False
>>> amstrang(407)
True
>>> amstrang(471)
False
>>> amstrang(371)
True
>>> 3**3+7**3+1**3
371
>>> for x in (1,3,8,0,6):
	print("ok",x)
print("fin")
SyntaxError: invalid syntax
>>> for x in (1,3,8,0,6):
	print("ok",x)

ok 1
ok 3
ok 8
ok 0
ok 6
>>> 
=  
>>> pgcd(4,20)
4
>>> pgcd(14,20)
2
>>> pgcd(13,20)
1
>>> 
=  
>>> pgcdM2(4,20)
4
>>> pgcdM2(14,20)
2
>>> pgcdM2(13,20)
1
>>> 
=  
>>> constE()
500
>>> 
=  
>>> constE()
2.7182818284590455
>>> 
=  
>>> 
=  
>>> L=[10,2,3,5,4,8,9,0,2,1,4,5,30]
>>> L
[10, 2, 3, 5, 4, 8, 9, 0, 2, 1, 4, 5, 30]
>>> type(L)
<class 'list'>
>>> L1=[10,20.5,"Ali",4+9j,[2,5,8],10,(10,20),{10,5},"A"]
>>> L1
[10, 20.5, 'Ali', (4+9j), [2, 5, 8], 10, (10, 20), {10, 5}, 'A']
>>> L
[10, 2, 3, 5, 4, 8, 9, 0, 2, 1, 4, 5, 30]
>>> L[0]
10
>>> L[1]
2
>>> L[-1]
30
>>> L[-2]
5
>>> L[1:4]
[2, 3, 5]
>>> L[1:]
[2, 3, 5, 4, 8, 9, 0, 2, 1, 4, 5, 30]
>>> L[:4]
[10, 2, 3, 5]
>>> L[:]
[10, 2, 3, 5, 4, 8, 9, 0, 2, 1, 4, 5, 30]
>>> L[]
SyntaxError: invalid syntax
>>> L[1:10:2]
[2, 5, 8, 0, 1]
>>> L[1:10:]
[2, 3, 5, 4, 8, 9, 0, 2, 1]
>>> L[1::]
[2, 3, 5, 4, 8, 9, 0, 2, 1, 4, 5, 30]
>>> L[::]
[10, 2, 3, 5, 4, 8, 9, 0, 2, 1, 4, 5, 30]
>>> L[::-1]
[30, 5, 4, 1, 2, 0, 9, 8, 4, 5, 3, 2, 10]
>>> L
[10, 2, 3, 5, 4, 8, 9, 0, 2, 1, 4, 5, 30]
>>> L[0]
10
>>> L[50]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    L[50]
IndexError: list index out of range
>>> L[50:100]
[]
>>> L
[10, 2, 3, 5, 4, 8, 9, 0, 2, 1, 4, 5, 30]
>>> L[0]=200
>>> L
[200, 2, 3, 5, 4, 8, 9, 0, 2, 1, 4, 5, 30]
>>> L[0:3]=[1,1,2,5,8,9,7,4]
>>> L
[1, 1, 2, 5, 8, 9, 7, 4, 5, 4, 8, 9, 0, 2, 1, 4, 5, 30]
>>> L[0:3]=[]
>>> L
[5, 8, 9, 7, 4, 5, 4, 8, 9, 0, 2, 1, 4, 5, 30]
>>> L[-5]
2
>>> L[-2]
5
>>> L[-5:-2]
[2, 1, 4]
>>> L[-5:-2:-1]
[]
>>> L[-2:-5:1]
[]
>>> L[-2:-5:-1]
[5, 4, 1]
>>> L
[5, 8, 9, 7, 4, 5, 4, 8, 9, 0, 2, 1, 4, 5, 30]
>>> 10 in L
False
>>> 4 in L
True
>>> L1
[10, 20.5, 'Ali', (4+9j), [2, 5, 8], 10, (10, 20), {10, 5}, 'A']
>>> 5 in L1
False
>>> L[4]
4
>>> L1[4]
[2, 5, 8]
>>> L1[4][-1]
8
>>> 5 in L1[4]
True
>>> 5 in L1[0]
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    5 in L1[0]
TypeError: argument of type 'int' is not iterable
>>> [1,2,5]+[4,5,8,7,9]
[1, 2, 5, 4, 5, 8, 7, 9]
>>> [1,2,5]+10
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    [1,2,5]+10
TypeError: can only concatenate list (not "int") to list
>>> [1,2,5]+[10]
[1, 2, 5, 10]
>>> [1,2,5]*5
[1, 2, 5, 1, 2, 5, 1, 2, 5, 1, 2, 5, 1, 2, 5]
>>> [1,2,5]*1
[1, 2, 5]
>>> [1,2,5]*0
[]
>>> [1,2,5]*(-5)
[]
>>> [1,2,5]*4.7
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    [1,2,5]*4.7
TypeError: can't multiply sequence by non-int of type 'float'
>>> [1,2,5]*[4,5,8]
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    [1,2,5]*[4,5,8]
TypeError: can't multiply sequence by non-int of type 'list'
>>> L
[5, 8, 9, 7, 4, 5, 4, 8, 9, 0, 2, 1, 4, 5, 30]
>>> len(L)
15
>>> max(L)
30
>>> min(L)
0
>>> sum(L)
101
>>> L.append(15)
>>> L
[5, 8, 9, 7, 4, 5, 4, 8, 9, 0, 2, 1, 4, 5, 30, 15]
>>> L.max()
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    L.max()
AttributeError: 'list' object has no attribute 'max'
>>> max(L)
30
>>> L.insert(0,105)
>>> L
[105, 5, 8, 9, 7, 4, 5, 4, 8, 9, 0, 2, 1, 4, 5, 30, 15]
>>> L.insert(2,105)
>>> L
[105, 5, 105, 8, 9, 7, 4, 5, 4, 8, 9, 0, 2, 1, 4, 5, 30, 15]
>>> L.index(15)
17
>>> L.pop()
15
>>> L
[105, 5, 105, 8, 9, 7, 4, 5, 4, 8, 9, 0, 2, 1, 4, 5, 30]
>>> L.pop(0)
105
>>> L
[5, 105, 8, 9, 7, 4, 5, 4, 8, 9, 0, 2, 1, 4, 5, 30]
>>> L.sort()
>>> L
[0, 1, 2, 4, 4, 4, 5, 5, 5, 7, 8, 8, 9, 9, 30, 105]
>>> L.sort(reverse=True)
>>> L
[105, 30, 9, 9, 8, 8, 7, 5, 5, 5, 4, 4, 4, 2, 1, 0]
>>> L2=[[105,"Hiba",15],[20,"Hind",13],[15,"Ali",11]]
>>> L2
[[105, 'Hiba', 15], [20, 'Hind', 13], [15, 'Ali', 11]]
>>> L2.sort()
>>> L2
[[15, 'Ali', 11], [20, 'Hind', 13], [105, 'Hiba', 15]]
>>> L2.sort(key=lambda x:x[2])
>>> L2
[[15, 'Ali', 11], [20, 'Hind', 13], [105, 'Hiba', 15]]
>>> L2.sort(key=lambda x:x[1])
>>> L2
[[15, 'Ali', 11], [105, 'Hiba', 15], [20, 'Hind', 13]]
>>> L2.sort(key=lambda x:x[2])
>>> L2
[[15, 'Ali', 11], [20, 'Hind', 13], [105, 'Hiba', 15]]
>>> max(L2)
[105, 'Hiba', 15]
>>> min(L2)
[15, 'Ali', 11]
>>> max(L2,key=lambda x:x[1])
[20, 'Hind', 13]
>>> max(L2,key=lambda x:x[2])
[105, 'Hiba', 15]
>>> l3=[[10,4,11],[10,9],[4,8,10,5]]
>>> L3.sort(key=lambda x:sum(x)/len(x))
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    L3.sort(key=lambda x:sum(x)/len(x))
NameError: name 'L3' is not defined
>>> l3.sort(key=lambda x:sum(x)/len(x))
>>> l3
[[4, 8, 10, 5], [10, 4, 11], [10, 9]]
>>> for x i, l3:
	
SyntaxError: invalid syntax
>>> for x in l3:
	print(sum)/len(x)

	
<built-in function sum>
Traceback (most recent call last):
  File "<pyshell#129>", line 2, in <module>
    print(sum)/len(x)
TypeError: unsupported operand type(s) for /: 'NoneType' and 'int'
>>> for x in l3:
	print(sum(x)/len(x))

	
6.75
8.333333333333334
9.5
>>> l3
[[4, 8, 10, 5], [10, 4, 11], [10, 9]]
>>> L
[105, 30, 9, 9, 8, 8, 7, 5, 5, 5, 4, 4, 4, 2, 1, 0]
>>> L.pop(1)
30
>>> L
[105, 9, 9, 8, 8, 7, 5, 5, 5, 4, 4, 4, 2, 1, 0]
>>> L[1]
9
>>> L[1]=[]
>>> L
[105, [], 9, 8, 8, 7, 5, 5, 5, 4, 4, 4, 2, 1, 0]
>>> L.pop(1)
[]
>>> L
[105, 9, 8, 8, 7, 5, 5, 5, 4, 4, 4, 2, 1, 0]
>>> L[1:2]=[]
>>> L
[105, 8, 8, 7, 5, 5, 5, 4, 4, 4, 2, 1, 0]
>>> L[-1]=5
>>> L
[105, 8, 8, 7, 5, 5, 5, 4, 4, 4, 2, 1, 5]
>>> L.remove(5)
>>> L
[105, 8, 8, 7, 5, 5, 4, 4, 4, 2, 1, 5]
>>> while 5 in L:
	L.remove(5)

	
>>> L
[105, 8, 8, 7, 4, 4, 4, 2, 1]
>>> L[1:3]=[]
>>> L
[105, 7, 4, 4, 4, 2, 1]
>>> L[5:5]=[100]
>>> L
[105, 7, 4, 4, 4, 100, 2, 1]
>>> L=[2*x for x in range(1:10,2)]
SyntaxError: invalid syntax
>>> L=[2*x for x in range(1,10,2)]
>>> L
[2, 6, 10, 14, 18]
>>> L=[2*x for x in range(10)]
>>> L
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> a,b=10,20
>>> a
10
>>> b
20
>>> a,b=b,a
>>> a
20
>>> b
10
>>> T=10,20
>>> type(T)
<class 'tuple'>
>>> T
(10, 20)
>>> 
================   ================
>>> L=[1,4,8,1,2,9,3,0,10]
>>> triBull(L)
>>> L
[0, 1, 1, 2, 3, 4, 8, 9, 10]
>>> L=[9,8,7,6,5,4]
>>> triBull(L)
>>> L
[4, 5, 6, 7, 8, 9]
>>> 
>>> L=[1,4,8,1,2,9,3,0,10]
>>> triBull(L)
>>> L
[0, 1, 1, 2, 3, 4, 8, 9, 10]
>>> L=[9,8,7,6,5,4]
>>> triBull(L)
>>> L
[4, 5, 6, 7, 8, 9]

>>> 
