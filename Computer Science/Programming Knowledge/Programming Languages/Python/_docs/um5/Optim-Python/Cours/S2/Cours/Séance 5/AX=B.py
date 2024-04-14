from numpy.linalg import solve


A=[[3,4,1],
   [5,1,1],
   [1,3,7]
   ]

B=[0,1,3]
X=solve(A,B)
print("x0=",X[0])
print("x1=",X[1])
print("x2=",X[2])
