frase="aqui me pongo a cantar"
palabra=""

for x in frase:
    if x != " ":
        palabra=palabra+x
    elif x == " ":
        print(palabra)
        palabra=""
print(palabra)
        
