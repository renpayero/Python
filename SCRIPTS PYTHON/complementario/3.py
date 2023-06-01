#cargado de funciones
from funciones3 import *
#inicializando diccionarios 
bebidas={}
mesas={}
for i in range(1,11):
    mesas[i]=[]
    
#inicio del programa
print('''Bienvenido al bar de moe
Seleccione la accion que desea realizar: ''')

#menu

while True:
    print('''
///////////////////////////////////////
(1) Cargar detalles de bebidas.
(2) Cargar consumo de una mesa.
(3) Ver listado de bebidas y precios.
(4) Cerrar mesa
(5) Termina el programa
///////////////////////////////////////''')

#comprobacion de ingreso
    while True:
        try:
            sel=int(input("Seleccion: "))
            if sel >=1 and sel <=5:
                break
            else:
                raise(ValueError)
        except(NameError):
            print("No se permiten caracteres")
        except(ValueError):
            print("Ingrese un numero entre 1 y 5")

#llamado a las funciones por seleccion
    if sel == 1:
        cargar(bebidas)
    elif sel == 2:
        cargarConsumo(mesas)
    elif sel == 3:
        listado(bebidas)
    elif sel == 4:
        mc=input("Mesa a cerrar: ")
        cerrarMesa(mc)
    elif sel == 5:
        break
    

    
