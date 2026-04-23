import os
os.system("CLS || CLEAR")

numeros = []

print("=== Busca de Número na Lista ===")
print("Digite 7 números:\n")

for i in range(1, 8):
    numero = int(input(f"Número {i}: "))
    numeros.append(numero)

busca = int(input("\nQual número você quer buscar? "))

print("\n--- Resultado ---")
print(f"Lista: {numeros}")

if busca in numeros:
    posicao = numeros.index(busca)
    print(f"Número encontrado!")
    print(f"Posição (índice) na lista: {posicao}")
else:
    print("Número não encontrado!")

numeros = []

print("=== Busca de Número na Lista ===")
print("Digite 7 números:\n")

for i in range(1, 8):
    numero = int(input(f"Número {i}: "))
    numeros.append(numero)

busca = int(input("\nQual número você quer buscar? "))

print("\n--- Resultado ---")
print(f"Lista: {numeros}")

if busca in numeros:
    posicao = numeros.index(busca)
    print(f"Número encontrado!")
    print(f"Posição (índice) na lista: {posicao}")
else:
    print("Número não encontrado!")