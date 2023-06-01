cadena=input("Ingrese una frase: ")
vocales = ""
if(cadena.find("a")!=-1):
    vocales += "a"
if(cadena.find("e")!=-1):
    vocales += "e"
if(cadena.find("i")!=-1):
    vocales += "i"
if(cadena.find("o")!=-1):
    vocales += "o"
if(cadena.find("u")!=-1):
    vocales += "u"
print(vocales)
