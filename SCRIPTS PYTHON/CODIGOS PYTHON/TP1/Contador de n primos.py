n1=int(input("Ingrese un numero mayor que 1 para inicializar el programa: "))
no=0
numprimo=0
numnoprimo=0

while n1 != 0:
    n1=int(input("Ingrese un numero mayor que 1: "))
    if n1 !=0:
        for x in range(2, n1):
            if ((n1%n1)== 0) and ((n1%1)==0):
                if ((n1%x)==0):
                    no+=1
            if no == 1:
                break
            else:
                continue
        if no == 0:
            numprimo+=1
        else:
            numnoprimo+=1

print("\nNumeros primos: ", numprimo, "\nNumeros no primos: ", numnoprimo)
