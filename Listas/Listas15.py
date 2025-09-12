lista = [10,20,30,40,50]
print("Lista:", lista)
num = int(input("Ingrese un número: "))
if num in lista:
    print("Está en la posición:", lista.index(num)+1)
else:
    print("No se encuentra en la lista")
