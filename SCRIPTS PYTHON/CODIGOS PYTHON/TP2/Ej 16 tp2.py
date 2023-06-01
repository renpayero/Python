cadena=input("Ingrese una frase")
digito=input("ingrese un digito")


for x in cadena:
    if x==digito:
        [x]="*"
print(cadena)
