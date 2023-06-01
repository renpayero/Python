nombres=[]
print("Ingrese los nombres")
while True:
    nom=input("")
    if nom == "":
        break
    nombres.append(nom)

for i in nombres:
    print(i)
