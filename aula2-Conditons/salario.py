import os
os.system('clear || cls')

# Questão 7 - Salario.

salario = float(input('Digite o salário do funcionário: '))

if salario >= 5000:
    print("O funcionário tem um salário alto.")
else:
    print("O funcionário tem um salário baixo.")