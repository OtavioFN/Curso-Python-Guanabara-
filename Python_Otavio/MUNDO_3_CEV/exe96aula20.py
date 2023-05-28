'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area(largura,comprimento):
    area = largura*comprimento
    print(f'{area:.2f}m²')

largura = float(input('Informe a largura do terreno em questão em metros: '))
comprimento = float(input('Informe o comprimento do terreno em questão em metros: '))
area(largura,comprimento)