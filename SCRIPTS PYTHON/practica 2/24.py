def moveChar (char, n):
    if char.isalpha():
        if char.isupper():
            char = chr(65+(((ord(char)-65)+n)%26))
        else:
            char = chr(97+(((ord(char)-97)+n)%26))
    return char

print("""Bienvenido al cifrado de césar

Seleccione la accion que desea realizar:

    1) Cifrar una frase
    2) Decifrar una frase
    Otro) Termina el programa
    """)

c=input("Seleccion: ")
while c == "1" or c == "2":
    lugares=0
    frasecesar=""
    if c=="1":
        print("Ingrese la frase que desea cifrar:")
        frase = input()
        while not(lugares >0):
            lugares = int(input("Ingrese la cantidad de lugares que desea mover (numero>0): "))
        for x in frase:
            frasecesar += moveChar(x, lugares)
        print("Frase cifrada: " + "'" +frasecesar+ "'")
    elif c=="2":
        print("Ingrese la frase que desea decifrar:")
        frase = input()
        while not(lugares >0):
            lugares = int(input("Ingrese la cantidad de lugares que se movio (numero>0): "))
        for x in frase:
            frasecesar += moveChar(x, -lugares)
        print("Frase cifrada: " + "'" +frasecesar+ "'")

    c2=input("Ponga C para continuar: ")
    if c2.upper() != "C":
        break
    print("""
Seleccione la accion que desea realizar:

    1) Cifrar una frase
    2) Decifrar una frase
    Otro) Termina el programa
    """)
    c=input("Seleccion: ")
