'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
ano_atual = date.today().year
dmaior = 0
dmenor = 0
for i in range(1,8):
    idade = int(input(f'Informe em que ano a {i}ª pessoa nasceu: '))
    if ano_atual - idade > 18:
        dmaior += 1
    else:
        dmenor += 1


print(f'''Ao todo, temos {dmaior} maiores de idade e {dmenor} menores!''')
        