def dos_sumados(lista,resultado):
    for i in lista:
        for j in lista:
            if (i + j) == resultado:
                return [lista.index(i),lista.index(j)]
