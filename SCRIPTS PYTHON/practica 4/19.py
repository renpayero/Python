def digitos_repetidos(n):
    digitos = set()
    repetidos = set()
    repetidos2 = []
    while n!=0:
        digito = n%10
        if digito in digitos:
            repetidos.add(digito)
            repetidos2.append(digito)
        digitos.add(digito)
        n = n//10
    
    return list(repetidos) if len(list(repetidos)) > 0 else None,repetidos2
ingresados=0

mayor_478=0
promedio=0

while True:
    suma=0
    repetidos=0

    numero=int(input("Ingrese un numero con digitos repetidos: \n"))
    dr_numeros,todosrep=digitos_repetidos(numero)

    if dr_numeros == None:
        break

    for i in todosrep:
        suma+=i

    if numero>478:
        mayor_478+=1
    
    repetidos=len(dr_numeros)
    promedio += numero
    ingresados+=1
    
    print("La suma de los digitos es repetidos:",suma)
    print(repetidos, "digito(s) repetidos")

print("El porcentaje de los numeros mayores a 478 es: %", ((mayor_478*100)/ingresados))
print("El promedio de los numeros ingresados es:", (promedio/ingresados))
