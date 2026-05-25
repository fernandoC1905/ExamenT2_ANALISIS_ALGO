import random

def buscarMaxMin(lista, pos, maximo, minimo):

    if pos == len(lista):
        return maximo, minimo

    if lista[pos] % 3 == 0:

        if lista[pos] > maximo:
            maximo = lista[pos]

        if lista[pos] < minimo:
            minimo = lista[pos]

    return buscarMaxMin(lista, pos + 1, maximo, minimo)

n = int(input("Ingrese el tamaño del arreglo: "))

lista = []

for i in range(n):
    num = random.randint(10, 9999)
    lista.append(num)

print("Lista:", lista)

maximo, minimo = buscarMaxMin(lista, 0, -99999, 99999)

print("Maximo numero multiplo de 3:", maximo)
print("Minimo numero multiplo de 3:", minimo)

promedio = (maximo + minimo) / 2

print("El promedio es:", promedio)