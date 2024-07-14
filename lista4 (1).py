
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

numprimos = 0
for numero in lista:
  primer_digito = int(str(abs(numero))[0]) # 
  if es_primo(primer_digito):
    numprimos += 1

print("Cantidad de números que comienzan con un dígito primo:", numprimos)