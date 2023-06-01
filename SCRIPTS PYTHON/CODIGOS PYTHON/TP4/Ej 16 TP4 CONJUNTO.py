conjunto=set(range(1,11))
conjunto.add(11)
conjunto.add(12)

conjunto2=set(range (30, 36))
conjunto=conjunto.union(conjunto2)
conjunto.add(232)
conjunto.add(-264)

if 7 in conjunto:
    print("El valor 7 esta en el conjunto")
else:
    print("El valor 7 no esta en el conjunto")
if 20 in conjunto:
    print("El valor 20 esta en el conjunto")
else:
    print("El valor 20 no esta en el conjunto")

print("La cantidad de elementos almacenados son", len(conjunto))
