def suma_digitos(n):
    suma=0
    while n!=0:
        suma+=n%10
        n=n//10
    return suma

def sumatoria_digitos(lista):
    newl=[]
    for i in lista:
        newl.append(suma_digitos(i))
    return newl
