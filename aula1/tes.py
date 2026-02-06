
#Aula 1 - Projeto Supermercado

print('Bem vindo ao superMERCADÃO!')

sabonete = 5.45
feijao = 7.99
cerveja = 5.50
arroz = 5.10
acucar = 4.20

qsabonete = int(input('Digite a quantidade de sabonetes: '))
qfeijao = int(input('Digite a quantos Kg de feijão: '))
qcerveja = int(input('Digite a quantidade de latinhas: '))
qarroz = int(input('Digite a quantos Kg de arroz: '))
qacucar = int(input('Digite a quantos Kg de açucar: '))


total = (sabonete * qsabonete) + (feijao * qfeijao) + (cerveja * qcerveja) + (arroz * qarroz) + (acucar * qacucar)

print(f'Valor total das suas comprar foi {total:.2f} reais.')