sucesion="0, 1"
contador=23
n1=0
n2=1
suma=str(n1+n2)

while contador!=0:
    n3=n1+n2
    n3=str(n3)
    sucesion=sucesion+", "+n3
    n3=int(n3)
    n1=n2
    n2=n3
    contador=contador-1
print(sucesion)
    
