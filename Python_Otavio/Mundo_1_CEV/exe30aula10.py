'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

numero = int(input('Digite um número qualquer: '))
if numero % 2 == 0:
    print(f'O número {numero} é \033[1;44mpar!\033[0m')
else:
    print(f'O número {numero} é \033[1;41mímpar!\033[0m')
