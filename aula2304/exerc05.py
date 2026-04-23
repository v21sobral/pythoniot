import os
os.system("CLS || CLEAR")

numeros = []

print("=== Removendo Valores Negativos ===")
print("Digite 8 números (positivos ou negativos):\n")

for i in range(1, 9):
    numero = int(input(f"Número {i}: "))
    numeros.append(numero)

positivos = [n for n in numeros if n >= 0]

removidos = len(numeros) - len(positivos)

print("\n--- Resultado ---")
print(f"Lista original:          {numeros}")
print(f"Lista sem negativos:     {positivos}")
print(f"Números removidos:       {removidos}")