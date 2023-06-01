from funciones import *
mayor=-1         
dni=int(input("DNI: "))    
while dni!=0:            
    if validar_dni(dni):
        nombre=input("Nombre: ")
        edad=int(input("Edad: "))
    if edad>mayor:
        mayor=edad
        nombre_mayor=nombre
    else:
        print("DNI inválido. Vuelva a ingresar.")
    dni=int(input("DNI: "))
print("Nombre de la persona mayor:", nombre_mayor)
