#Supermercado Coto


''' Formato

Codigo de producto: x

Tipo: x
(1) Lacteo
(2) Almacen
(3) Verduleria
(4) Limpieza
(5) Carniceria
(6) Otros

Descripcion:
x

Stock Actual: x
Stock Minimo: x
Precio Unitario: $x


'''

#Inicio de Diccionarios

productos={}

detalles={"tipo":0,
          "desc":"",
          "stock":0,
          "min_stock":0,
          "precio":0.00}

tipo_producto={1:"Lacteo",
               2:"Almacen",
               3:"Verduleria",
               4:"Limpieza",
               5:"Carniceria",
               6:"Otros"}

#Inicio de Variables
codigo=0
tipo = 0
desc = ""
stock = 0
min_stock = 0
precio = 0


#Inicio del programa

print("/"*50,''' 
Bienvenido al programa de registro de productos COTO

Ingrese el codigo del producto que desea añadir a continuacion.
'''+"/"*50,"\n") #Escribe un mensaje de bienvenida


while True:
    tipo = 0
    desc = ""
    stock = 0
    min_stock = 0
    precio = 0
    #//// Codigo de producto

    while True:     #Comprueba que se ingrese un valor de tipo correcto, si no devuelve un error y pide reingreso.
        try:
            codigo=int(input("\nCodigo: " )) #Ingreso del codigo
            break
        except ValueError:
            print("\n    Error: Ingrese un codigo valido (-1 para terminar)")

    if codigo == -1:
        break 

    #////Ingreso del Tipo de producto
            
    print(
'''\nIngrese el tipo de producto:
(1) Lacteo
(2) Almacen
(3) Verduleria
(4) Limpieza
(5) Carniceria
(6) Otros''')
    
    while True:     #Comprueba que se ingrese un valor de tipo correcto, si no devuelve un error y pide reingreso.
        try:
            tipo=int(input("\nTipo: " ))    
            if tipo <1 or tipo >6:
                raise(ValueError)
            break
        except ValueError:
            print("\n    Error: Ingrese un tipo de producto valido (1 al 6)")


    #////Ingreso de la descripcion de producto

    
    print("\nIngrese la descripcion del producto (No puede estar vacia)\n")
    while desc == "": #Comprueba que no se ingrese una descripcion vacia
        desc=input() 


    #////Ingreso de la cantidad en Stock
        

    while True:     #Comprueba que se ingrese un valor de tipo correcto, si no devuelve un error y pide reingreso.
        try:
            stock=int(input("\nCantidad en stock del producto: " ))    #Ingreso del stock
            if stock <0:
                raise(ValueError)
            break
        except ValueError:
            print("\n    Error: Ingrese una cantidad valida")


    #////Ingreso del stock minimo


    while True:     #Comprueba que se ingrese un valor de tipo correcto, si no devuelve un error y pide reingreso.
        try:
            min_stock=int(input("\nCantidad minima de stock del producto: " ))    #Ingreso del stock
            if min_stock <0:
                raise(ValueError)
            break
        except ValueError:
            print("\n    Error: Ingrese una cantidad valida")


    #////Ingreso del precio por unidad


    while True:     #Comprueba que se ingrese un valor de tipo correcto, si no devuelve un error y pide reingreso.
        try:
            precio=float(input("\nPrecio unitario: $" ))    #Ingreso del valor en numero entero
            if precio <0:
                raise(ValueError)
            break
        except ValueError:
            print("\n    Error: Ingrese un precio valido")

    print("\n"+"/"*50,"\n        Ingreso del producto",codigo,"completo\n"+"/"*50+"\nSiguiente ingreso a continuacion")

    #Asignacion de los detalles
    detalles["tipo"]=tipo
    detalles["desc"]=desc
    detalles["stock"]=stock
    detalles["min_stock"]=min_stock
    detalles["precio"]=precio

    #Ingreso del producto al dicc. con sus detalles.
    productos[codigo]=dict(detalles)

print("\n"+"/"*50,"\n        Ingreso de productos finalizado\n"+"/"*50+"\n")

#a)
if 124 in productos and productos[124]["stock"] > productos[124]["min_stock"]:
    print("Se puede vender una unidad del producto 124")
else:
    print("No se puede vender")

#b)
print("Los productos debajo del stock minimo: ")
for i in productos:
    if productos[i]["stock"]<productos[i]["min_stock"]:
        print("Codigo: ", i, " Descripcion: ",productos[i]["desc"])

#c)
lacteos = 0
for i in productos:
    if productos[i]["tipo"]==1:
        lacteos += 1

print("Cantidad de prod. lacteos: ", lacteos)

#d)
menorstock = 999999999
codigoprod = 0
for i in productos:
    if productos[i]["stock"]<menorstock:
        menorstock = productos[i]["stock"]
        codigoprod = i
print("Producto con menor stock: ", codigoprod)

#e)
      
if 3148 in productos:
    print("La descripcion del producto 3148 es:", productos[3148]["desc"] )
else:
    print("El producto 3148 no existe")

#f)
menorstock = 999999999
codigoprod = 0
venta = productos[i]["stock"]-productos[i]["min_stock"]
for i in productos:
    if venta<menorstock:
        menorstock = venta
        codigoprod = i
        
print("Producto con menor stock a la venta: ", codigoprod)
