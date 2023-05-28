'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep

pv = int(input('Informe o primeiro valor: '))
sv = int(input('Informe o segundo valor: '))
fim = False
while not fim:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opçao = int(input('>>> Qual a sua opção: '))
    if opçao == 1:
        print(f'A soma entre {pv} e {sv} resulta em {pv+sv}')
        sleep(1)
    elif opçao == 2:
        print(f'O produto entre {pv} e {sv} resulta em {pv*sv}')
        sleep(1)
    elif opçao == 3:
        if pv > sv:
            print(f'{pv} é o maior dos números!')
            sleep(1)
        else: 
            print(f'{sv} é o maior dos números')
            sleep(1)
    elif opçao == 4:
        pv = int(input('Informe um novo número para o primeiro valor: '))
        sv = int(input('Informe um novo número para o segundo valor: '))
        sleep(1)
    elif opçao == 5:
        fim = True
        sleep(1)
    else: 
        print('Opção inválida, tente novamente!')
        sleep(1)
print('Programa finalizado!')

