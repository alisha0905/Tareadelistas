#9 Leer 10 números enteros, almacenarlos en una lista y calcular la factorial a cada uno de los números leídos almacenándolos en otra lista

lista = []
contador = 0
while contador < 10:
  lista.append(int(input("Ingrese un numero: ")))
  contador += 1


def factorial(numero):
  if numero == 0:
    return 1
  else:
    fact = 1
    for i in range(1, numero + 1):
      fact *= i
    return fact

factoriales =[]
for numero in lista:
  factoriales.append(factorial(numero))


print(factoriales)