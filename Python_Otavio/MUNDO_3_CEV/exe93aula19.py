'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

player = dict()
gols = 0
player['nome'] = str(input('Informe o nome do jogador: '))
player['partidas'] = int(input('Informe quantas partidas o jogador jogou: '))
for i in range(player['partidas']):
    player[f'partida{i+1}'] = int(input(f'Informe quantos gols o jogador fez na {i+1}º partida: '))
    gols += player[f'partida{i+1}']
player['gols'] = gols
print(player)
