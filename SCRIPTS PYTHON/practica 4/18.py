def digitos_repetidos(n):
    digitos = set()
    repetidos = set()
    while n!=0:
        digito = n%10
        if digito in digitos:
            repetidos.add(digito)
        digitos.add(digito)
        n = n//10
    
    return list(repetidos)
