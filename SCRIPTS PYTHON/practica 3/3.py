from funciones import es_par
pares = 0
positivos = True
n=int(input("Ingrese un numero: "))
while pares < 7:
    if n < 0:
        positivos = False
    if n%2==0:
        pares += 1
    n=int(input("Ingrese un numero: "))    
print("Todos los ingresados son positivos" if positivos else "Alguno de los ingresados fue negativo")
