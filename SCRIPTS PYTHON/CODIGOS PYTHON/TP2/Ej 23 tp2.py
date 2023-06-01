var="HOla como estas"
abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
condicional=0
for x in range(4):
    if(var[x] in abc):
        condicional+=1
if(condicional>=2):
	print(var.upper())
