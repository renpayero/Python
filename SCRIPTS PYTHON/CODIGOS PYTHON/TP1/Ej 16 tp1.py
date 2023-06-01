frase="Usar programas es genial, pero ¡hacerlos es lo mejor!"

#A
(frase[32:37]+" "+frase[37:40]+frase[4:15]+frase[41:]).capitalize()
#Al ejecutar la linea de codigo anterior tomaremos las siguientes rebanadas de
#la string frase
# "hacer" "los" "programas" "es" "lo" "mejor!" y con capitalize pondremos
#la primera letra en mayusculas
#IMPORTANTE: Notar que los parentesis encierran los comandos que tomaran
#las rebanadas, por lo que el capitalize lograra identeficiar cual es la
#string a la que tiene que aplicar la mayusculas

#B
518273//(len(frase)*4)%2==0

#La linea de codigo anterior tomara la longitud de la string FRASE,
#Luego la multiplicara por 4, dividira el numero en 2 y tomara su resto
#Su resto va a ser dividido por 518273 y solo se tendra en cuenta la parte int
#y luego lo comparara con 0 y dara un valor de verdad ya sea true si es
#igual a 0 o false si es distinto de 0
#EL RESULTADO SERA TRUE

#C
frase[len(frase)-1]
#Se le restara 1 a la longitud de la string "frase" y se imprimira la letra
#Que le corresponda a dicha posicion
#En este caso imprimira el ultimo digito "!" debido a que la longitud de la
#cadena es 53 pero la posicion se comienza a contar desde 0 o sea que si no
#restamos el 1 nos dara error ya que el digito no estara en nuestra
#cadena de caracteres

