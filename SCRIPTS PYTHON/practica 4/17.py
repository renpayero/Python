horm1 = set(["melanina", "oxitocina", "dopamina" ])
horm2 = set(["testosterona", "melanina"])
horm3 = set (["calcinotna", "estradiol"])

(horm1 & horm2)

horm2 < horm1

hormonas = horm1|horm2|horm3
for x in hormonas:
    print(x)
