from sqlite3 import *
from pandas import *
def afficher(bd,req):
    c=connect(bd)
    cur=c.cursor()
    res=cur.execute(req)
    for x in res:
        print(x)
    c.close()

def afficher02(bd,req):
    c=connect(bd)
    cur=c.cursor()
    res=cur.execute(req)
    print(DataFrame(res,columns=["Nom","Prenom"]))
    c.close()
"""
#afficher("G_ Etudiants.sqlite","select nom,prenom,section from etudiants")
afficher02("G_ Etudiants.sqlite","select nom,prenom from etudiants")

"""
c=connect("BD01.sqlite")
cur=c.cursor()
req1="create table Etudiants(num int,nom str,primary key(num))"
req2="insert into etudiants values(10,'Ali'),(20,'Sara'),(30,'Ali')"
cur.execute(req1)
cur.execute(req2)
#c.commit()
c.close()



