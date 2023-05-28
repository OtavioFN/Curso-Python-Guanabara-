'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''
velocidade = float(input('Informe a velocidade do carro: '))
if velocidade <= 80.0:
    print('\033[42mBoa noite, tenha uma boa viagem!\033[0m')
else:
    print(f'Você foi multado e terá que pagar a multa de R$ \033[4;41m{(velocidade-80)*7:.2f} reais!\033[0m')
