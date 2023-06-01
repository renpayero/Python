frase = input("Ingrese una frase: ")
frase = frase.strip()
palabras = frase.split(" ")
for x in palabras:
    if(x!="" and x!=" "):
        print(x)
