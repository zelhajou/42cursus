"""
f=open("exemple02.txt","w")
f.write("Bonjour\\nMes etudiants")
f.close()

f=open("exemple01.txt","r")
print(f.readlines())

f.close()
"""

#ex01
def copier01(fich1,fich2):
    f=open(fich1,"r")
    g=open(fich2,"w")
    c=f.read(1)
    while c!="":
        g.write(c)
        c=f.read(1)
    f.close()
    g.close()
    
def copier02(fich1,fich2):
    f=open(fich1,"r")
    g=open(fich2,"w")
    c=f.readline()
    while c!="":
        g.write(c)
        c=f.readline()
    f.close()
    g.close()   
    
def copier03(fich1,fich2):
    f=open(fich1,"r")
    g=open(fich2,"w")
    s=f.read()
    g.write(s.upper())
    f.close()
    g.close()

def copier04(fich1,fich2):
    f=open(fich1,"r")
    g=open(fich2,"w")
    s=f.read()
    for x in s:
        if x not in ("\n"," ","\t"):
            g.write(chr(ord(x)+1))
        else:
            g.write(x)
    f.close()
    g.close()
def RC4Fichier(fich, Clef, fichChiffre):
    f=open(fich,"r")
    g=open(fichChiffre,"w")
    Claire=f.read()
    ch=RC4Chaine(Claire,Clef)
    g.write(ch)
    f.close()
    g.close()
    










    
