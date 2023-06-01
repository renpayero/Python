contador=20
negativos=0
sumnegativos=0
positivos=0
sumpositivos=0
ceros=0
while contador != 0:
    n1=int(input("Ingrese un numero entre -10 y 10: "))
    while n1 <= -10:
        print("Su valor es menor o igual a -10 porfavor ingrese un nuevo valor: ")
        n1=int(input("-"))
    while n1 >= 10:
        print("Su valor es mayor o igual a 10 porfavor ingrese un nuevo valor: ")
        n1=int(input("-")) 
    if n1 < 0:
        negativos=negativos+1
        sumnegativos=sumnegativos+n1
    elif n1 == 0:
        ceros=ceros+1
    elif n1 > 0:
        positivos=positivos+1
        sumpositivos=sumpositivos+n1
    contador=contador-1
    
print("\nLa cantidad de numeros negativos ingresados es ", negativos, "y la suma de ellos es igual a ", sumnegativos,"\nLa cantidad de numeros positivos ingresados es ", positivos,"y la suma de ellos es igual a ", sumpositivos,"\nLa cantidad de numeros iguales a cero es ", ceros)
        
        
    
    
