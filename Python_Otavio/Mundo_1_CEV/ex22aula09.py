# Exercício 22
#Crie um programa que leia o nome de uma pessoa e mostre:
# 1) O nome da pessoa com todas as letras maiúsculas
# 2) O nome da pessoa com todas as letras minúsculas
# 3) Quantas letras tem ao todo (sem considerar os espaços)
# 4) Quantas letras tem o primeiro nome

# Atividade extra: cores
class colors:
    redl = '\033[31m'
    bluel = '\033[34m'
    yellowl = '\033[33m'
    cyanl = '\033[36m'
    greenl = '\033[32m'
    magental = '\033[35m'
    clean = '\033[0m'

nome = str(input('Digite seu nome completo: ')).strip()
#1)
print(f'Seu nome em letras maiúsculas é {colors.redl}{nome.upper()}{colors.clean}')
#2)
print(f'Seu nome em minúsculas é {colors.bluel}{nome.lower()}{colors.clean}')
#3)
'''print(f'Você tem {len(nome.replace(" ",""))} letras em seu nome')'''
# Ou
print(f'Você tem {colors.yellowl}{len(nome) - nome.count(" ")}{colors.clean} letras em seu nome')
#4)
print(f'Seu primeiro nome é {colors.cyanl}{nome.split()[0]}{colors.clean} e tem {colors.greenl}{len(nome.split()[0])}{colors.clean} letras em seu primeiro nome')
''' OU - nome_dividido = nome.split()
print(f'Seu primeiro nome é {nome_dividido[0]} e tem {len(nome_dividido[0])} letras em seu primeiro nome')'''
# OU
print(f'Seu primeiro nome tem {colors.magental}{nome.find(" ")}{colors.clean} letras')