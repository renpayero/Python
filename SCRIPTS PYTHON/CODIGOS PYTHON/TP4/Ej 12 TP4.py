from funciones import*
def sumatoria_digitos(lista):
    numeros=[]
    for x in lista:
        numeros.append(suma_digitos(x))
    print(numeros)
    
    
