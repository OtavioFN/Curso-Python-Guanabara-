# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# Atividade extra cores
colors = {'greenl':'\033[32m', 'redl':'\033[31m', 'yellowl':'\033[33m', 'bluel':'\033[34m', 'clean':'\033[0m'}

number = int(input('Digite um número de 0 a 9999: '))
unit = number % 10
group_of_ten = number // 10 % 10 
hundred = number // 100 % 10 
thousand = number // 1000 % 10
print(f'''Analisando o número {number} ...
Unidade: {colors['greenl']}{unit}{colors['clean']}
Dezena: {colors['redl']}{group_of_ten}{colors['clean']}
Centena: {colors['yellowl']}{hundred}{colors['clean']}
Milhar: {colors['bluel']}{thousand}{colors['clean']}''')