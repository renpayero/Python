from funciones import*
contador=8
pares=0

while contador!=0:
    if es_par(int(input("ingrese un entero"))):
        contador=contador-1
        pares=pares+1
if pares==8:
    print("todos los numeros ingresados fueron pares")
    
        
    
