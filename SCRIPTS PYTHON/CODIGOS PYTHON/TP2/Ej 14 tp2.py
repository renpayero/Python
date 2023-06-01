pares=0
impares=0
cincos=0
n1="0"
while n1 != "-1":
    n1=input("Ingrese un numero entero positivo: ")
    while n1!="-1":
        for x in n1:
            if((int(x))%2)==0:
                pares=pares+1
            elif((int(x))%2)!=0:
                impares=impares+1
                if (int(x))==5:
                    cincos=cincos+1
                
        break
    
print("\nLa cantidad de numeros pares es", pares,"\nLa cantidad de numeros impares es", impares,"\nLa cantidad de cincos en los numeros procesados es ", cincos)

               

                  
       
        
    
    
