#Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
from random import choice
opções = [1,2,3]
print('''Suas opções
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
escolha_comp = choice(opções)
escolha = int(input('Sua opção: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
if escolha == 1:
    if escolha_comp == 1:
        print('''Você escolheu pedra
O computador escolheu pedra
Empate!''')
    elif escolha_comp == 2:
        print('''Você escolheu pedra
O computador escolheu papel
O computador venceu!''')
    elif escolha_comp == 3:
        print('''Você escolheu pedra
O computador escolheu tesoura
Você venceu!''')
    else:
        print('Jogada inválida!')
elif escolha == 2:
    if escolha_comp == 1:
        print('''Você escolheu papel
O computador escolheu pedra
Você venceu!''')
    elif escolha_comp == 2:
        print('''Você escolheu pedra
O computador escolheu pedra
Empate!''')
    elif escolha_comp == 3:
        print('''Você escolheu pedra
O computador escolheu tesoura
Você venceu!''')
    else:
        print('Jogada inválida!')
elif escolha == 3:
    if escolha_comp == 1:
        print('''Você escolheu tesoura
O computador escolheu pedra
O computador venceu!''')
    elif escolha_comp == 2:
        print('''Você escolheu tesoura
O computador escolheu papel
Você venceu!''')
    elif escolha_comp == 3:
        print('''Você escolheu tesoura
O computador escolheu tesoura
Empate!''')
    else:
        print('Jogada inválida!')
else:
    print('Jogada inválida!')
'''Dicas
Itens = ['pedra', 'papel', 'tesoura'] 
computador = random.randint(1, 3)
print(f'O computador jogou {itens[computador]}'''