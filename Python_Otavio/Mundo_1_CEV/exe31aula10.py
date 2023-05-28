''' Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.'''
from re import A


distancia = float(input('Informe a distância da viagem em Km: '))
if distancia <= 200:
    cobrança = 0.50
    passagem = distancia*cobrança
    print(f'O preço de uma passagem para uma viagem de {distancia} Km será de R$ {passagem:.2f} !')
else:
    cobrança = 0.45
    passagem = distancia*cobrança
    print(f'O preço de uma passagem para uma viagem de {distancia} Km será de R$ {passagem:.2f} !')
print('Tenha uma boa viagem !')