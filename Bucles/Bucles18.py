texto = input("Ingrese un texto: ")
nuevo = ""
for letra in texto:
    if letra == " ":
        nuevo += "-"
    else:
        nuevo += letra
print(nuevo)
