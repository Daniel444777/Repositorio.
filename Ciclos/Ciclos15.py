secreto = 7
adivinado = False
while not adivinado:
    intento = int(input("Adivina el número: "))
    if intento == secreto:
        print("¡Correcto!")
        adivinado = True
    else:
        print("Intenta de nuevo.")