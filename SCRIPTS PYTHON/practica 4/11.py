def ocurrencia(lista):
    elem=[]
    nuevalista=[]
    for i in lista:
        if i not in elem:
            elem.append(i)
            nuevalista.append([i,lista.count(i)])
    return nuevalista
