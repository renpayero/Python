ciudad=[
    ["Rosario","SantaFe"],
    ["CarlosPaz","Córdoba"],
    ["Balcarce","BuenosAires"],
    ["Cosquín","Córdoba"]
    ]

listapersonas=[
    ["JuanPerez",26782345,"CarlosPaz"],
    ["MaríaGomez",40173542,"Rosario"],
    ["AnaRíos",9216378,"Cosquín"]
    ]


def obtenerCiudad(personas, DNI):
    for i in personas:
        if i[1]==DNI:
            return i[2]
    return "No se encontro el DNI" + DNI + "en la lista."

def obtenerProvincia(personas, ciudades, DNI):
    ciu=obtenerCiudad(personas, DNI)
    for i in ciudades:
        if i[0] == ciu:
            return i[1]

def contarPoblacion(personas, ciudades, provincia):
    poblacion=0
    for i in personas:
        prov = obtenerProvincia(personas, ciudades, i[1]).lower()
        if prov == provincia.lower():
            poblacion+=1
    print("La poblacion de la provincia", provincia, "es: ", poblacion)
        
    
