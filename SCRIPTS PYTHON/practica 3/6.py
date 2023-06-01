from funciones import suma_digitos
from funciones import es_par
pares=0
impares=0
print("El programa finalizara al leer un numero que la suma de sus digitos sea menor a 10 o mayor que 50")
while True:
    numero=int(input("Ingrese un numero :"))
    if(es_par(numero)):
        pares+=1
    else:
        impares+=1
    if suma_digitos(numero)<10 or suma_digitos(numero)>50:
        break
print("Ingresos pares: ", pares, "\nIngresos Impares: ", impares)
