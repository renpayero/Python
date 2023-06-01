#Da ERROR
#fruta = "manzana" 
#longitud = len(fruta) 
#última = fruta[longitud]


#Genera un error porque en longitud se guarda el carácter 7 y si bien la cadena de fruta tiene 7 caracteres,
#al buscar la posición numero 7 genera un error ya que Python cuenta desde el 0 y la posición 7 es el carácter
#6 en la cadena fruta.
#Para que funcione debería ser algo así:
fruta='manzana'
longitud=len(fruta)-1
ultima=fruta[longitud]
