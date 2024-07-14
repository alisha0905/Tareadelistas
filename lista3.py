def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

lista = []
contador = 0
while contador < 10:
  lista.append(int(input("Ingrese un numero: ")))
  contador += 1

mayor_primo = -1  
posicion = -1

for i, num in enumerate(lista):
  if is_prime(num):
    if num > mayor_primo:
      mayor_primo = num
      posicion = i+1

print("El numero mayor primo es", mayor_primo, "y esta en la posicion", posicion)