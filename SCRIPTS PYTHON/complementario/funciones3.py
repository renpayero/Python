def cargar(bebidas):
    print("\nIngreso de bebidas, x para terminar")
    while True:
        bebida=input("Bebida: ").title()
        if bebida == "X":
            break
        precio=float(input("Precio: "))
        while precio <= 0:
            print("El precio no puede ser menor o igual a 0")
            precio=float(input("Precio: "))
        bebidas[bebida]=precio

def cargarConsumo(listaMesas):
    print("\nCargar consumo")
    mesa=int(input("Mesa: "))
    while mesa <1 or mesa>10:
        print("Numero de mesa incorrecto, reingrese.")
        mesa=int(input("Mesa: "))
    print("Ingrese consumos (x para terminar)")
    while True:
        consumo=input("Bebida: ").title()
        if consumo == "X":
            break
        listaMesas[mesa] += [consumo]

def listado(bebidas):
    if len(bebidas) > 0:
        for i,j in bebidas.items():
            print("Bebida: "+str(i)+"   Precio: "+str(j))
    else:
        print("No hay bebidas ingresadas")

def cerrarMesa(mesa):
    total=0
    for i in mesas[mesa]:
        print("Bebida: " + str(i) + " Precio: "+ str(bebidas[i]))
        total+=bebidas[i]
    print("Total: $"+str(total))
    mesas[mesa]=[]
