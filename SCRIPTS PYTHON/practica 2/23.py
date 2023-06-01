frase = input("Ingrese una frase: ")
maycount = 0
for x in range (0,4):
    if(frase[x].isupper()):
        maycount += 1

if(maycount>=2):
    print(frase.upper())
else:
    print(frase)
