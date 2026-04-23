import os
os.system("CLS || CLEAR")


idades = []

print("=== Cadastro de Idades ===")
print("Digite -1 para encerrar.\n")

while True:
    entrada = int(input("Digite uma idade: "))

    if entrada == -1:
        break

    idades.append(entrada)

print("\n--- Resultado ---")
print(f"Idades digitadas: {idades}")
print(f"Quantidade de idades: {len(idades)}")

if len(idades) > 0:
    media = sum(idades) / len(idades)
    maiores = len([i for i in idades if i >= 18])
    print(f"Média das idades: {media:.1f}")
    print(f"Idades >= 18 anos: {maiores}")
else:
    print("Nenhuma idade foi informada.")