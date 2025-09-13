palabra = "programacion"
contador = 0
for letra in palabra:
    if letra in "aeiou":
        contador += 1
print("Cantidad de vocales:", contador)