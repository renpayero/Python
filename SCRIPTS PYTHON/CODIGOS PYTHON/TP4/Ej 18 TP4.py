def digitos_repetidos(n):
    listanueva=[]
    for x in n:
        cantidad=n.count(x)
        if cantidad>=2:
            listanueva.append(x)
    lista2=set(listanueva)
    print(lista2)
            
        
    
