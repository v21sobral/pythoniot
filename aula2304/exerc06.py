import os
os.system("CLS || CLEAR")

numeros = []

print("=== Maior e Menor com Posição ===")
print("Digite 5 números:\n")

for i in range(1, 6):
    numero = int(input(f"Número {i}: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

posicao_maior = numeros.index(maior)
posicao_menor = numeros.index(menor)

print("\n--- Resultado ---")
print(f"Lista: {numeros}")
print(f"Maior valor: {maior}  →  posição {posicao_maior}")
print(f"Menor valor: {menor}  →  posição {posicao_menor}")