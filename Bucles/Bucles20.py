lista = [5,-3,7,-1,0,8,-6]
positivos = 0
negativos = 0

for num in lista:
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("Positivos:", positivos)
print("Negativos:", negativos)
