cantalumnos=int(input("Ingrese la cantidad de alumnos: "))
aprobados=0
desaprobados=0

while cantalumnos!=0:
    nota=int(input("Ingrese la nota del alumno: "))
    if nota >= 4:
        aprobados=aprobados+1
    elif nota<4:
        desaprobados=desaprobados+1
    cantalumnos=cantalumnos-1
    
print("\nLa cantidad de aprobados es ", aprobados, "\nLa cantidad de aprobados es ", desaprobados)
    
        
