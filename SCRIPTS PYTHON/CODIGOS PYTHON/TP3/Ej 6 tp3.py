from funciones import*
impar=0
num=int(input("ingrese algo: "))
while(num!=0):
	if(suma_digitos(num)>10 and suma_digitos(num)<50):
		if(es_par(num)==False):
			impar=impar+1
	else:
		break
	num=int(input("ingrese algo: "))
print(impar)
