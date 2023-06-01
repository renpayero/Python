from funciones import usuario
from funciones import contrasenia_por_defecto
while True:
    print("Ingrese su nombre de usuario:")
    nombre=input()
    if ("juan" in nombre.lower() or "maría" in nombre.lower()):
        break
    print("Ingrese su Nº Documento")
    contrasenia=int(input())
    print("Su usuario de unnoba virtual es: ", usuario(nombre))
    print("Su contraseña de unnoba virtual es: ", contrasenia_por_defecto(contrasenia))
    
    
