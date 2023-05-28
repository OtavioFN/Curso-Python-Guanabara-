# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

import colorama as c

num = int(input('Informe um número: '))
div = 0
for i in range(1,num+1):
    if num % i == 0:
        print(c.Fore.YELLOW + f'{i}' + c.Style.RESET_ALL, end=' ')
        div += 1
    else: 
        print(c.Fore.RED + f'{i}' + c.Style.RESET_ALL, end=' ')
print()
print(f'O número {num} foi divisível {div} vezes')
if div == 2:
    print('E por isso ele é um número PRIMO!')
else: 
    print('E por isso ele NÃO é PRIMO!')