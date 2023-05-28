'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))

if r1 + r2 < r2 or r3 + r2 < r1 or r1 + r3 < r2:
    print('As retas não formam um triângulo')
elif r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    if r1 == r2 == r3:
        print('Esse é um triângulo Equilátero!')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
        print('Esse é um triângulo Isósceles!')
    elif r1 != r2 != r3 != r1:
        print('Esse é um triângulo Escaleno!')