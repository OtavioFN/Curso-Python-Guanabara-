'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto'''
# todos os anos múltiplos de 4 que também não são múltiplos de 100
from datetime import date
ano = int(input('Informe o ano a ser analisado ou digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year # importa o ano atual mostrado no computador
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')