letras="abcdefghijklmnñopqrstuvxwyzáéíóú "
numeros="1234567890"
ingresos=0
mayus=0
simbol=False
print("Ingrese cadenas de caracteres, terminando el programa al ingresar un 0")
while True:
    cadena = input()
    if "0" in cadena:
        break
    for i in cadena:
        if i.lower() not in letras and i.lower() not in numeros:
            simbol = True
        if i.isupper():
            mayus += 1
    if simbol:
        print("Contiene simbolos")
    else:
        print("No contiene simbolos")
    ingresos += 1

print("Se ingreso " + str(ingresos) + " cadena(s)")
print("Hubo en total " + str(mayus) + " letra(s) mayuscula(s)")

    
