n=input("Ingrese un nombre")
nombres=[]
nmay=[]
while n != " ":
    nombres.append(n)
    n=input("Ingrese un nombre")

for x in nombres:       #CONVIERTE LOS NOMBRES INGRESADOS EN EL WHILE A MAYUS
    nmay.append(x.upper())

print(nmay)

