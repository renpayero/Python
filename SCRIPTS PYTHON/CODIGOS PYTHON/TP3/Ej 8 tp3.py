def usuario(apellido, nombre):
    nombre=nombre.lower()
    apellido=apellido.lower()
    nombre=nombre.replace(" ", "")
    apellido=apellido.replace(" ", "")
    print(nombre+apellido)

def contra(dni):
    dni=dni%10000
    return dni



    
    
