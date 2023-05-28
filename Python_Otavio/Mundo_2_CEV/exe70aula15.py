'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

gasto_total = 0
produtos_1000 = 0
mais_barato = 0
nome_mais_barato = ''
contador = 0 
while True:
    nome = str(input('Informe o nome do produto: '))
    preço = float(input('Preço: R$'))
    contador +=1 
    gasto_total += preço
    if contador == 1 or preço < mais_barato: 
        mais_barato = preço
        nome_mais_barato = nome
#    if preço < mais_barato:
#        mais_barato = preço
#        nome_mais_barato = nome
    if preço > 1000:
        produtos_1000 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print('=====PROGRAMA ENCERRADO=====')
if gasto_total == 0:
    print('Não houve gasto nas compras!')
else:
    print(f'O gasto total das compras foi de R${gasto_total:.2f} ')
if produtos_1000 == 0:
    print('Não houve produtos mais caros que mil reais!')
elif produtos_1000 == 1:
    print('Houve somente um produto mais caro que mil reais!')
else:
    print(f'Houve {produtos_1000} produtos mais caros que mil reais!')
print(f'O produto mais barato foi o(a) {nome_mais_barato}, custando R${mais_barato:.2f} ')
    
    
