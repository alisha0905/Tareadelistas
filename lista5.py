# 5. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición se encuentra el número primo con mayor cantidad de dígitos pares.

lista = []
contador = 0
while contador < 10:
  lista.append(int(input("Ingrese un numero: ")))
  contador += 1

def es_primo(numero):
  if numero <= 1:
    return False
  for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
      return False
  return True

def contar_digitos_pares(numero):
  contador = 0
  while numero > 0:
    digito = numero % 10
    if digito % 2 == 0:
      contador += 1
    numero //= 10
  return contador

mayorpares = -1
posicion_mayorpares = -1

for i, numero in enumerate(lista):
  if es_primo(numero):
    cantidad_pares = contar_digitos_pares(numero)
    if cantidad_pares > mayorpares:
      mayor_primo_pares = cantidad_pares
      posicion_mayor_primo_pares = i

if posicion_mayor_primo_pares != -1:
  print("El número primo con más dígitos pares es", lista[posicion_mayorpares], "en la posición", posicion_mayorpares)
else:
  print("No se encontraron números primos en la lista.")