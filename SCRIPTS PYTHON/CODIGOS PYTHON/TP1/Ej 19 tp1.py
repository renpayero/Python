a = ' Python es un lenguaje amigable para empezar a aprender programación '
b = ' nociones básicas de '

#A
print ("La longitud de la cadena A es:", len(a))

#B
print("La palabra amigable se encuenta en la posicion",  a.find("amigable"))

#C
print((a[56:]).capitalize()) #capitalize() pone la primera letra en mayuscula

#D
c=a.lstrip(" ")
print(c.rstrip(" "))

#E
e=a[1:54]+b+a[56:-1]
print(e)

#F
a=a.replace("amigable", "AMIGABLE") #Reemplaza la palabra amigable en minusculas por la misma en mayusculas
d=a[23:31]
e.replace("amigable", d)
print(e.replace("amigable", d))





