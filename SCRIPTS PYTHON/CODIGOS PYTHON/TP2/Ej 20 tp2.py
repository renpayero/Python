var=input("Ingrese un solo caracter distinto de 0 para empezar el programa")
var2=""
var3="l"
zetas=0

while var != "0":
    var=input("Ingrese un caracter: ")
    if len(var)==len(var3):
        if var == "z":
            zetas=zetas+1
        var2=var2+var
if var[-1]=="0":
    var2=var2.rstrip("0")
print("\nEl string formado es", var2, "\nLa cantidad de zetas en el string es ", zetas)
        
    
    

