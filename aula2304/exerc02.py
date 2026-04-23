import os
os.system("CLS || CLEAR")

numeros = []

print("=== Contador de Pares e Ímpares ===")
print("Digite 6 números inteiros:\n")

for i in range(1, 7):
    numero = int(input(f"Número {i}: "))
    numeros.append(numero)

pares = 0
impares = 0

for n in numeros:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\n--- Resultado ---")
print(f"Lista digitada: {numeros}")
print(f"Números pares:  {pares}")
print(f"Números ímpares: {impares}")