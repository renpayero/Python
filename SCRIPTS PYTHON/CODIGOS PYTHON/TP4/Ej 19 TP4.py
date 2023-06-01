from funciones import*

def numeros_iguales(n):
    n=str(n)
    n2=1
    global digitos
    digitos=""
    for x in n:
        cant=n.count(x)
        if cant >= 2:
            digitos+=x
    digitos=int(digitos)


def numeros_igualesbool(n):
    n=str(n)
    n2=1
    for x in n:
        cant=n.count(x)
        if cant >= 2:
            return True
    return False

enteros=int(input("Ingrese numeros enteros"))
numeros_procesados=0

while numeros_igualesbool(enteros):
    numeros_procesados=numeros_procesados+1
    numeros_iguales(enteros)
    suma_digitos=suma_digitos(digitos)
    
    print("La suma de los digitos repetidos es", suma_digitos)
    cantidad_que_aparece=digitos.count(len(0))
    
    print("La cantidad de veces que aparece", digitos[1], "En el numero entero ingresado es", cantidad_que_aparece)
    enteros=int(input("Ingrese numeros enteros"))
    
    





        
    
