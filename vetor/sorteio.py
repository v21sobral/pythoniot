import os
os.system('clear || cls')

import random

numeros = [23, 44, 56, 74, 1, 21 , 33]
nomes = ['Amanda', 'Mariana', 'Emy', 'Fernanda']

# append() - Adiciona um elemento ao final da lista.
# insert() - Adiciona um elemento em uma posição específica da lista.

# -----------------------------------------------------------------------

# pop() - Remove o último elemento da lista e o retorna.
# remove() - Remove a primeira ocorrência de um elemento específico da lista.

# ------------------------------------------------------------------------

# sort() - Ordena os elementos da lista em ordem crescente.
# reverse() - Inverte a ordem dos elementos da lista (sem ordenar), mas se for usado após sort(), ele ordena em ordem decrescente.
# len() - Quantos elementos existem na lista.
# max() - Retorna o maior elemento da lista.
# min() - Retorna o menor elemento da lista tambem utilizadp para strings.
# sum() - Retorna a soma de todos os elementos da lista (apenas para listas de números).
# random.choice() - Retorna um elemento aleatório da lista.

sorteado = random.choice(nomes)
print(f'O nome sorteado foi: {sorteado}.')