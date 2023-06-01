from funciones import*

nombre=input("ingrese nombre: ")
while(nombre!="maria" and nombre!="juan"):
    apellido=input("ingrese apellido: ")
    contra=contra(int(input("ingrese su dni")))
    print(usuario(apellido,nombre))
    print (contra)
    nombre=input("ingrese nombre: ")
	
