cadena=input("Ingrese un texto: ")
letra=input("Ingrese una letra que se encuentre en el texto: ")
cadena2=""

for x in cadena:
    if x==letra:
        cadena2=cadena2+"*"
    elif x!=letra:
        cadena2=cadena2+x
print(cadena2)
