import os
os.system('clear || cls')

# Questão 4 - Comparação de números.

a = int(input('digite o primeiro número: '))
b = int(input('digite o segundo número: '))

if a > b:
    print('O primeiro número é maior que o segundo.')
elif b > a:
    print('O segundo número é maior que o primeiro.')
else:
    print('Os números são iguais.')