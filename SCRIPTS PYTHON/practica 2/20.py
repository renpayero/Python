print("Ingrese 1 caracter a la vez, mas o 0 para finalizar")
cara = input()
string = ""
while cara != "0" and len(cara) <=1:
    string +=cara
    cara = input()
if len(string)!=0:
    print("Se forma:", string)
    print("porcentaje de 'z' : %", (string.count("z")*100)/len(string))
