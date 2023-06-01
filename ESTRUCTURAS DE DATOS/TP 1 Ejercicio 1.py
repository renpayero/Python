x=[1,2,3,4,5,6,7,8,9,10]
i=0
fin=len(x)
busc=7
medio=int((i + fin)/2)
if x[medio]==busc:
    print("Valor Encontrado En El Medio")
else:
    while medio<=fin or medio!=x[i]:
        if x[medio]<busc:
            print("Valor Mas Grande")
            if x[medio]==busc:
                print("la posicion es: ", medio)
                break
            medio+=1
            continue
        else:
            if x[medio]==busc:
                print("la posicion es:",medio)
                break
            medio-=1
            

            
            
            
