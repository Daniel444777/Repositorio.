tupla = (1, 2, 3, 4)
try:
    tupla[0] = 10
except TypeError as e:
    print("Error al modificar la tupla:", e)
