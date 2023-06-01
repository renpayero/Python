def minimo_elemento(lista):
    if lista == []:
        return None
    elem = lista[0]
    for i in lista:
        if i < elem:
            elem = i
    return elem
