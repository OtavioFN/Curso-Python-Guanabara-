'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)'''

import colorama
from colorama import Fore
from colorama import Style

colorama.init()

def leiaInt(ask):
    num = str(input(ask))
    while num.isnumeric() == False:
        print(Fore.RED + 'ERRO! Digite um número inteiro válido: ' + Style.RESET_ALL)
        num = str(input(ask))
    return num




n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')