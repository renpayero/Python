libro = input("Ingrese el titulo de su libro preferido: ")
cap = ""
for x in range(0,len(libro)-1):
    if x==0:
        cap += libro[x].upper()
    else:
        cap += libro[x].lower()

print(cap)
    
