def maximo(num_1, num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2


var1=maximo(int(input("int")), int(input("int")))
var2=maximo(int(input("int")), int(input("int")))
var3=maximo(int(input("int")), int (input("ingrese un 0")))

var4=maximo(var1, var2)
maximo=maximo(var4, var3)

print(maximo)
