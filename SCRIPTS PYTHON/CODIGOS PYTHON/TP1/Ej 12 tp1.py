cadena1 = "¡Bienvenidos!"
cadena2 = " esto es"
cadena3 = " IPI"
cadena4 = " lo más divertido"
cadena5 = " de primer año"
cadena6 = " ..."

#A Construir la cadena "Bienvenidos esto es de primer año lo más divertido... IPI".
cadena1=cadena1.strip("¡!")
cadenac=cadena1+cadena2+cadena5+cadena4+cadena6+cadena3

#B
cadenac.find("primer") #Esta en la posicion 23

#C
cadena1.find("e") #Como anteriormente sacamos los signos de admiracion a cadena1 y las posiciones
                    #se cuentan desde 0 la primera posicion en la que se encuentra e es en la 2
                    #si no hubieramos sacado los signos de admiracion estaria en la posicion 3

#D
cadena1.find("n") #Como anteriormente sacamos los signos de admiracion a cadena1 y las posiciones
                     #se cuentan desde 0 la primera posicion en la que se encuentra e es en la 3
                     #si no hubieramos sacado los signos de admiracion estaria en la posicion 4

#E
for x in cadena6:
    x == " "

    #En el codigo anterior estamos recorriendo cada x de cadena6 ejecutando el operador logico de igualdad,
    #cuando x sea igual a un espacio dara true, cuando no, dara false

#F
cadena4[:6].find("d")
#Se obtiene el resultado -1 porque en la posicion 6 de cadena4 no esta la letra d y no puede recorrer mas parte de
#la cadena por la instruccion/restriccion [:6]

#G
cantespacios=0    #inicializamos la variable para luego sumar
for x in cadenac:
    if x==" ":
        cantespacios=cantespacios+1
print(cantespacios)
        

    


