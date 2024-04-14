def ajouterEtudiant(E,num,nom,ville):
    E[num]=[nom,ville]

def ajouterMatieres(M,code,nom,coef):
    M[code]=[nom,coef]

def ajouterExamen(EX,num,code,note):
    EX[(num,code)]=note

def moyenneEtudiant(E,EX,M,num):
    if num in E:
        sn=0
        sc=0
        for k in EX:
            if k[0]==num:
                sn+=EX[k]*M[k[1]][1]
                sc+=M[k[1]][1]
        return sn/sc
    else:
        return "etudiant n'existe pas"
def afficherNote(M,EX,num):
    for k in EX:
        if k[0]==num:
            print(M[k[1]][0],EX[k])
        
#(15*5+10*9)/14

E={}
M={}
EX={}
ajouterEtudiant(E,1,"Ali","Rabat")
ajouterEtudiant(E,2,"Sara","Rabat")
ajouterEtudiant(E,3,"Hind","Rabat")
ajouterEtudiant(E,4,"Mohamed","Rabat")

ajouterMatieres(M,101,"JAVA",5)
ajouterMatieres(M,102,"PYTHON",9)
ajouterMatieres(M,103,"C",10)
ajouterMatieres(M,105,"C++",5)

ajouterExamen(EX,1,101,15)
ajouterExamen(EX,1,102,10)
ajouterExamen(EX,2,101,16)
ajouterExamen(EX,3,101,13)
