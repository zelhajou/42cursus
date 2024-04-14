"""
chapitre La POO(Les classes)
1) Les Classes prédéfinies
    int
    float
    complex
    bool
    str
    list
    set
    tuple
    dict
    ...
2) Les classes non définies

class Nom_Classe:
    def m1(p1,p2,...,pn):
        .....
        
    def m2(p1,p2,...,pn):
        .....
        
    def m3(p1,p2,...,pn):
        .....
        
        .
        .
        .
    def mn(p1,p2,...,pn):
        .....
def f1(p1,p2,...,pn):
        .....
def f1(p1,p2,...,pn):
        .....
.
.
.
def fn(p1,p2,...,pn):
        .....
"""

class point:
    def __init__(p,a=0,b=0):
        p.x=a
        p.y=b
    def afficher(p):
        print(p.x,p.y)
    #def __str__(p):
    #    return "("+str(p.x)+","+str(p.y)+")"
    def __repr__(p):
        return "("+str(p.x)+","+str(p.y)+")"
    def repr02(p):
        return "["+str(p.x)+","+str(p.y)+"]"
    def add(A,B):
        return point(A.x+B.x,A.y+B.y)
    def __add__(A,B):
        return point(A.x+B.x,A.y+B.y)
    def __mul__(A,B):
        return point(A.x*B.x,A.y*B.y)
    def dist01(p):
        return (p.x**2+p.y**2)**0.5
def dist02(p):
    return (p.x**2+p.y**2)**0.5



    

