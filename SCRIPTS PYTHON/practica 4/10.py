def borrar_adyacentes(lista):
    l=[]
    conj=set()
    for i in lista:
        conj.add(i)
    for elem in conj:
        l.append(elem)
    return l
