'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
from time import sleep
'''while True:
    computador = randint(0,10)
    imppar = ' '
    while imppar not in 'PI':
        imppar = str(input('Informe sua escolha [I/P]: ')).strip().upper()
    numero = int(input('Informe um número entre 1 e 10: '))
    if (numero+computador)%2 == 0:
        if imppar == 'P':
            print(f'O computador escolheu o número {computador}')
            print('Parabéns, você ganhou!')
        else:
            print(f'O computador escolheu o número {computador}')
            break
    elif imppar == 'I':
        print(f'O computador escolheu o número {computador}')
        print('Parabéns, você ganhou!')
    else:
        print(f'O computador escolheu o número {computador}')
        break
print('Você perdeu!')'''

vitorias = 0
computador = randint(0,10)
while True:
    opçao = ' '
    while opçao not in 'PI':
        opçao = str(input('Escolha se você deseja ser par ou ímpar [P/I]: ')).strip().upper()
    numero = int(input('Informe um número entre 0 e 10: '))
    while numero > 10 or numero < 0:
        numero = int(input('Informe um número entre 0 e 10: '))
    total = numero + computador
    if total % 2 == 0:
        if opçao == 'P':
            print('...')
            sleep(0.5)
            print(f'Parabéns, o valor final resultou em {total}, você ganhou!')
            vitorias += 1
        else:
            print('...')
            sleep(0.5)
            print(f'O resultado final deu em {total}, infelizmente você perdeu!')
            break
    else:
        if opçao == 'I':
            print('...')
            sleep(0.5)
            print(f'Parabéns, o valor final resultou em {total}, você ganhou!')
            vitorias += 1
        else:
            print('...')
            sleep(0.5)
            print(f'O resultado final deu em {total}, infelizmente você perdeu!')
            break
if vitorias == 0:
    print('Infelizmente você perdeu e não obteve nenhuma vitória')
elif vitorias == 1:
    print('Infelizmente você perdeu, mas antes disso você conseguiu obter uma vitória')
else:
    print(f'O programa acabou, antes de perder você ganhou {vitorias} vezes seguidas!')

