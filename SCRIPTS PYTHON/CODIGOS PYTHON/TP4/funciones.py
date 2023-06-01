def es_par(numero):
  if(numero%2==0):
         return True
  return False

def suma_digitos(numero):
    acu=0
    while numero!=0:
        acu=acu+(numero%10)
        numero=numero//10
    return acu

def maximo(num_1, num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2

def usuario(apellido, nombre):
    nombre=nombre.lower()
    apellido=apellido.lower()
    nombre=nombre.replace(" ", "")
    apellido=apellido.replace(" ", "")
    n=nombre+apellido
    print(n)

def contra(dni):
    dni=dni%10000
    return dni

def prueba(x, y):
  print(x, y)
  x=x+1
  y=y+2
  return(x, y)

def prueba(a,b):
  a=a+1
  b=b+2
  return(a,b)

def validar_dni(dni):
  cantidad=0
  while dni!=0:
    cantidad = cantidad + 1
    dni = dni//10
  return cantidad==8

def minimo_elemento(lista):
    l=lista[1]
    while lista != []:
        for x in lista:
            if x<l:
                l=x
        return (l)


