def sumatoriaRecursiva(lista):
    aux=0

    def sumar(lista,aux):
        if len(lista)==0:
            return aux
        else:
            aux+=lista[0]
            return sumar(lista[1:],aux)
    return sumar(lista,aux)
