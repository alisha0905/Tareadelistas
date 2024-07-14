#6.Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se encuentran los números con más de 3 dígitos

lista = []
contador = 0
while contador < 10:
  lista.append(int(input("Ingrese un numero: ")))
  contador += 1

posiciones = []  

for i, numero in enumerate(lista):
  if len(str(abs(numero))) > 3: 
    posiciones.append(i+1)

if posiciones:
  print("Los números con más de 3 dígitos se encuentran en las posiciones:", posiciones)
else:
  print("No se encontraron números con más de 3 dígitos en la lista.")