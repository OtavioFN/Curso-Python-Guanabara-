'''Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 

OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_1 = 0
while True:
    print('='*30)
    print(f'{"BANCO XRC":^30}')
    print('='*30)
    valor = int(input('Informe o valor que você quer sacar: R$'))
    notas_50 = valor // 50
    valor -= notas_50*50
    if valor > 20:
        notas_20 = valor//20
        valor -= notas_20*20
    if valor > 10:
        notas_10 = valor//10
        valor -= notas_10*10
    if valor > 1:
        notas_1 = valor//1
        valor -= notas_1
    break
if notas_50 != 0:
    print(f'Total de {notas_50} cédulas de R$50')
if notas_20 != 0:
    print(f'Total de {notas_20} cédulas de R$20')
if notas_10 != 0:
    print(f'Total de {notas_10} cédulas de R$10')
if notas_1 != 0:
    print(f'Total de {notas_1} cédulas de R$1')
print('='*20)