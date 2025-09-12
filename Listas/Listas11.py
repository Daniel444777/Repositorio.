lista = [10,20,30,40,50]
print("Lista:", lista)
num = int(input("Ingrese el número que quiere eliminar: "))
if num in lista:
    lista.remove(num)
    print("Lista actualizada:", lista)
else:
    print("Ese número no está en la lista")
