def indice_mayor(lista):
    aux=0
    for i in lista:
       if i > aux:
           aux = i
    return lista.index(aux)
