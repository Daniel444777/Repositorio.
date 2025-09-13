frase = "la casa es blanca"
letra = "a"
contador = 0
for c in frase:
    if c == letra:
        contador += 1
print(f"La letra '{letra}' aparece {contador} veces.")