def suma_digitos(numero):
    acu=0
    while numero!=0:
        acu=acu+(numero%10)
        numero=numero//10
    return acu
