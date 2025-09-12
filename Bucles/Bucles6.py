palabra = input("Ingrese una palabra: ")
contador = 0
for letra in palabra:
    if letra.lower() in "aeiou":
        contador += 1
print("La palabra tiene", contador, "vocales")
