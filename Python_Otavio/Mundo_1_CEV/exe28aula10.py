'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
import random as r
from time import sleep # Faz o computador "dormir"
numero = r.randint(1,10)
numero_chutado = int(input('Digite um número entre \033[35m1 e 10\033[0m: '))
print('\033[36mVerificando resposta...\033[0m')
sleep(3)
if numero == numero_chutado:
    print('Parabéns, você acertou!')
else:
    #print(f'Que pena, você errou! O número sorteado foi {numero}, e não {numero_chutado} !')
#EXPANSÃO IRAN---
    if numero_chutado < numero:
        print('\033[31m' + 'Que pena,' f' o número sorteado é maior que {numero_chutado}' + '\033[0m')
        print('Vamos tentar novamente?')
        numero_chutado = int(input(f'Digite um número entre \033[35m{numero_chutado+1} a 10\033[0m: '))
    
    else:
        print('\033[31m' + 'Que pena, ' + f'o número sorteado é menor que {numero_chutado}' + '\033[0m')
        print('\033[33m' + 'Vamos tentar novamente?' + '\033[0m')
        numero_chutado = int(input(f'Digite um número entre \033[35m1 a {numero_chutado-1}\033[0m: '))
    if numero == numero_chutado:
        print('\033[32m' + 'Você acertou!' + '\033[0m')
    else:
        print('\033[31m' + 'Você errou!' + '\033[0m')