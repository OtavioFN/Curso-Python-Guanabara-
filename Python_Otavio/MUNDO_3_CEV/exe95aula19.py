'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

player = dict()
jogador = list()
while True:
    resume = ''
    gols = 0
    player['nome'] = str(input('Informe o nome do jogador: '))
    player['partidas'] = int(
        input('Informe quantas partidas o jogador jogou: '))
    for i in range(player['partidas']):
        player[f'partida{i+1}'] = int(
            input(f'Informe quantos gols o jogador fez na {i+1}º partida: '))
        gols += player[f'partida{i+1}']
    player['gols'] = gols
    jogador.append(player.copy())
    player.clear()
    resume = str(input('Do u want to continue? [Y/N]: ')).strip().upper()
    while resume not in 'YN':
        resume = str(input('Do u want to continue? [Y/N]: ')).strip().upper()
    if resume == 'N':
        break
print(f'{"Cód":<5}{"Nome":<5}')
for num, jog in enumerate(jogador):
    print(f'{num:<5}{jog["nome"]:<5}')
num = 0
while num != 999:
    cod_nome = int(input('Digite o código do jogador que você deseja saber detalhes [digite 999 pra parar]: '))
    if cod_nome == 999:
        break
    else:
        print(f'Com {jogador[cod_nome]["gols"]} gols em {jogador[cod_nome]["partidas"]} partidas, o aproveitamento de {jogador[cod_nome]["nome"]} foi de {(jogador[cod_nome]["gols"]/jogador[cod_nome]["partidas"])*100:.1f}%')
        for num, jog in enumerate(jogador):
            print(f'{num:<5}{jog["nome"]:<5}')
print('Programa encerrado!')