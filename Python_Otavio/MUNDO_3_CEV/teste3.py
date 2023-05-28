'''import turtle
ninja = turtle.Turtle()
ninja.speed(10)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(30)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)
turtle.done()'''

'''matriz = [[0,0,0],[0,0,0],[0,0,0]]

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição {linha+1, coluna+1}: '))

for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()'''        

'''def is_isogram(string):
    if string == '':
        return True
    else:
        data = list()
        for num, i in enumerate(string.strip().upper()):
            if i in data:
                return False
            else:
                data.append(i)
                if num == len(string) and data[-1] != i:
                    return True

print(is_isogram('BOKJgltuQ'))'''

'''def is_isogram(string):
    if string == '':
        return True
    else:
        for i in string.upper():
            if string.count(i) > 1:
                return False
            else:
                return True'''

'''print(is_isogram('BOKJgltuQ'))'''

'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

'''player = dict()
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
while True:
    print(f'{"Cód":<5}{"Nome":<5}')
    for num, jog in enumerate(jogador):
        print(f'{num:<5}{jog["nome"]:<5}')
    cod_nome = int(input('Digite o código do jogador que você deseja saber detalhes [digite 999 pra parar]: '))
    if cod_nome == 999:
        break
    else:
        print(f'Com {jogador[cod_nome]["gols"]} gols em {jogador[cod_nome]["partidas"]} partidas, o aproveitamento de {jogador[cod_nome]["nome"]} foi de {(jogador[cod_nome]["gols"]/jogador[cod_nome]["partidas"])*100:.1f}%')
print('Programa encerrado!')'''

'''print(f'{"Otávio":^50}')
for i in range(10,-1,-2):
    print(i)'''

'''from datetime import date

ano_atual = date.today().year
print(ano_atual)'''

'''a = 12.34
print(a%100)'''

'''numero = str(input('Digite um número: '))
if numero.replace(',','').isnumeric() == True:
    numero = numero.replace(',','.')
    print('Corrigimos seu número')
    numero = float(numero)
    print(numero/2)
else:
    print('Seu programa deu erro')'''


'''num1 = '12.5'
num1 = float(num1)
print(num1/2)'''

'''num = [1,2,2]
for a,b in enumerate(num):
    print(a)'''

'''x = 3
y = 4
z = 5
if ((x-1)>2):
    y = y -1
z = x + y
for i in range(8):
    y = y + 1
z = z + y
print(z)

otavio& = 9'''


v[2+4]
9
v[8-v[2]]
v[8-6]
v[2]
6
v[v[v[7]]]
v[v[1]]
v[2]
6
v[v[1] * v[4]]
v[6]
9

    