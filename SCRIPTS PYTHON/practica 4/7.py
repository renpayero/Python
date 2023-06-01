def minimo_elemento(lista):
    if lista == []:
        return None
    elem = lista[0]
    elem2 = int
    for i in lista:
        if i < elem:
            elem = i
    for i in lista:
        if i > elem and i < elem2:
            elem2 = i
    if(elem2==elem):
        elem2=None
    return elem,elem2
