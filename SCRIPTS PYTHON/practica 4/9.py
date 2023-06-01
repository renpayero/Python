def digitos(numero):
    lista=[]
    while numero != 0:
        lista.append(numero%10)
        numero=numero//10
    return lista[::-1]
    
