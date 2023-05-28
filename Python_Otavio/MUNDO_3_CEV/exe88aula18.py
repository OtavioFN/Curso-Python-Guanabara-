'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from random import *
games = int(input('Tell the number of games you want to play: '))
data = []
jogo = []
for game in range(games):
    for i in range(6):
        while len(data) < 6:
            number = randint(1,60)
            if number not in data:
                data.append(number)
    data.sort()
    jogo.append(data[:])
    data.clear()

print(f'Os números sorteados foram: ')
for num,game in enumerate(jogo):
    print(f' Jogo {num+1} game')

