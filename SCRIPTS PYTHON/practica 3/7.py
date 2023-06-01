from funciones import maximo
digito=0
maximo_d=0
print("Ingrese 5 digitos positivos")
for i in range(5):
    digito=int(input())
    while digito<0:
        print("Mayores a 0 por favor.")
        digito=int(input())
    maximo_d = maximo(digito,maximo_d)
print(maximo_d)
    
