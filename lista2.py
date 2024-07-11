#1. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número leído.

lista = []
contador= 0
while contador<10:
  lista.append(int(input("Ingrese un numero: ")))
  contador += 1

numeromayor= max(lista)
posicion= lista.index(numeromayor)
posicion =posicion+1 

print("El numero mayor es ", numeromayor, " y esta en la posicion", posicion)
  