cadena = input("Ingrese una frase: ")
cadena2 = ""
caracter = input("Ingrese un caracter: ")
caracter = caracter[0]

for i in cadena:
    if i.lower() == caracter.lower():
        cadena2 += "*"
    else:
        cadena2 += i
    
print(cadena2)
