import  pickle as p
"""
f=open("exemple07.txt","wb")
x=[100,200,300,400]
p.dump(x,f)
f.close()
"""
f=open("exemple07.txt","rb")
x=p.load(f)
print(x)
f.close()

