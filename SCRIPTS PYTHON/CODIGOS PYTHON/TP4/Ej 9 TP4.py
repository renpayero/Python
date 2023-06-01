def digitos(numero):
    n=[]
    while numero!=0:
        n.append(numero%10)
        numero=numero//10
    return(n)
