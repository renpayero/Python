n1=int(input("ingresar un numero entero"))
sumapar=0
sumaimpar=0
    
if n1 > 0:
    while n1 != 0:
        n2=int(input("Ingrese un numero"))
        while n2 < 0:
            print("no.")
            n2=int(input("Ingrese un numero"))
        if (n2%2) == 0:  
            sumapar+=n2
        elif (n2%2) != 0:
            sumaimpar+=n2
        n1-=1
print("La suma de los numeros impares es", sumaimpar, " y la suma de los numeros pares es ", sumapar)
