def indice_mayor(lista):
    mayor=lista[0]
    indice=0
    for x in range(len(lista)):
        if (lista[x] > mayor):
            mayor=lista[x]
            indice=x
            
    print(indice)

        
    
