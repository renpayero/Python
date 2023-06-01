monto=1
cantidad=0
while monto!=0:
    monto=int(input("Ingrese las ganancias de la semana"))
    if monto < 0:
        monto=int(input("El numero ingresado no puede ser negativo, porfavor ingrese uno nuevo"))
    elif monto>0:
        cantidad=cantidad+monto

print("La cantidad recaudada con las ventas es", cantidad)
    
