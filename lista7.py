#7Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual el promedio entero de los datos de la lista

lista = []
contador = 0
while contador < 10:
  lista.append(int(input("Ingrese un numero: ")))
  contador += 1


promedio= sum(lista)/len(lista)


print("El promedio es", promedio)