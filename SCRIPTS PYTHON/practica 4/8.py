def piedra_papel_tijera(uno,dos):
    uno=uno.strip().lower()
    dos=dos.strip().lower()
    if uno == dos:
        return 0
    if uno == "piedra" and dos == "tijera":
        return 1
    if uno == "papel" and dos == "piedra":
        return 1
    if uno == "tijera" and dos == "papel":
        return 1
    if uno == "tijera" and dos == "piedra":
        return 2
    if uno == "piedra" and dos == "papel":
        return 2
    if uno == "papel" and dos == "tijera":
        return 2
