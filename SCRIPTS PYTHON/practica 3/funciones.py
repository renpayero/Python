def es_par(n):
    return n%2==0

def suma_digitos(n):
    suma=0
    while n!=0:
        suma+=n%10
        n=n//10
    return suma

def maximo(a,b):
    return a if a > b else b

def usuario(nombre):
    nom=""
    for x in nombre:
        nom += x if x != " " else ""
    nom = nom.lower()
    nom = nom.split(",")
    return nom[1]+nom[0]

def contrasenia_por_defecto(documento):
    return documento%10000

def titulo(cadena):
    espacio=True
    titulo=""
    for x in cadena:
        if x==" ":
            espacio=True
        else:
            if espacio == True:
                x=x.upper()
                espacio=False
        titulo+=x
    return titulo
