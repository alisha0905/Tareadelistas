#10.   Leer 10 números enteros, almacenarlos en una lista. Luego leer un entero y determinar cuántos divisores exactos tiene este último número entre los valores almacenados en la lista.

lista = []
contador = 0
while contador < 10:
  lista.append(int(input("Ingrese un numero: ")))
  contador += 1
ultimonumero= lista[-1]

divisores = 0
for i in lista:
  if ultimonumero % i == 0:
    divisores +=1


print("El numero", ultimonumero, "tiene", divisores, "divisores exacto")
  