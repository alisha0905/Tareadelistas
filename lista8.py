#8Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números negativos hay.

lista = []
contador = 0
numnegativo= 0
while contador < 10:
  lista.append(int(input("Ingrese un numero: ")))
  contador += 1

for i in lista:
  if i < 0:
    numnegativo += 1


print("Hay", numnegativo, "numeros negativos")