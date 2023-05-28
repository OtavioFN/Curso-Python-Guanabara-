'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from operator import itemgetter

ranking = dict()
players = dict()
players['player1'] = randint(1,6)
players['player2'] = randint(1,6)
players['player3'] = randint(1,6)
players['player4'] = randint(1,6)

print('Valores sorteados:')
for k, v in players.items():
    print(f'{k} tirou {v} no dado.')
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
print(ranking)
for num, i in enumerate(ranking):
    print(f'{num+1}º lugar: {i[0]} com {i[1]} pontos')
    