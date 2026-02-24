import os
os.system('clear || cls')

# Questão 6 - Par ou Ímpar.

numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é ímpar.')