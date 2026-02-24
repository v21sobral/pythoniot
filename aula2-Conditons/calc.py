import os
os.system('clear || cls')

# Questão 8 - Calculadora.

primeiroNumero = int(input('Digite o primeiro número: '))
segundoNumero = int(input('Digite o segundo número: '))
operacao = input('Digite a operação (+, -, *, /): ')

if operacao == '+':
    resultado = primeiroNumero + segundoNumero
    print(f'A soma foi: {resultado}')
elif operacao == '-':
    resultado = primeiroNumero - segundoNumero 
    print(f'A subtração foi: {resultado}')
elif operacao == '*':
    resultado = primeiroNumero * segundoNumero
    print(f'A multiplicação foi: {resultado}')
elif operacao == '/':
    if segundoNumero != 0 and primeiroNumero != 0:
        resultado = primeiroNumero / segundoNumero
        print(f'A divisão foi: {resultado}')
    else:
        print('Erro: Divisão por zero não é permitida.')
else:
    print('Operação inválida. Por favor, escolha entre +, -, * ou /.')