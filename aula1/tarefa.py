print('Bem vindo ao sistema de notas SENAI!')
nome = input('Digite o seu nome: \n')
nota1 = float(input('Digite sua 1º nota: '))
nota2 = float(input('Digite sua 2º nota: '))
nota3 = float(input('Digite sua 3º nota: '))

media = (nota1 + nota2 + nota3)/3

print(f'{nome} sua média foi {media:.2f}')
