horm1 = set(['melanina', 'oxitocina', 'dopamina'])
horm2 = set(['testosterona', 'melanina'])
horm3 = set(['calcinotna', 'estradiol'])

#A
if horm1.intersection(horm2):
    comun=horm1.intersection(horm2)
    print("horm1 y horm2 comparten", comun)
else:
    print("horm1 y horm2 no comparten un choto no fueron a jardin")
if horm1.intersection(horm3):
    comun2=horm1.intersection(horm3)
    print("horm1 y horm3 comparten", comun2)
else:
    print("horm1y horm3 no comparten un choto no fueron a jardin")

#B
if horm2 in horm1:
    print("horm2 es un subconjunto de horm1 alto metido lol")
else:
    print("horm2 no es un subconjunto de horm1, hace la suya el cra")

#C
horm1=horm1.union(horm2)
horm1=horm1.union(horm3)
for x in horm1:
    print(x)
