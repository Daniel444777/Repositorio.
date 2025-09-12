lista = [10,20,30,40,50]
print("Lista:", lista)
a = int(input("Posición del numerador (1-5): "))
b = int(input("Posición del denominador (1-5): "))

if lista[b-1] != 0:
    print("La división es:", lista[a-1] / lista[b-1])
else:
    print("Error: división por cero")
