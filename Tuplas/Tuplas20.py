tupla = (100,200,300)
try:
    tupla.append(400)
except AttributeError as e:
    print("Error, las tuplas no tienen append:", e)
