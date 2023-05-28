'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8'''

'''#Minha resposta

contador = int(input('Informe quantos elementos da sequência deseja ver: '))
anterior = 0
proximo = 1
while contador > 0:
    if contador > 1:
        print(f'{anterior} - ', end='')
    else:
        print(f'{anterior}')
    anterior, proximo = proximo, proximo + anterior
    contador -= 1
'''

# GUANABARA

contador = int(input('Informe quantos números da sequência deseja ver: '))
anterior = 0
proximo = 1
print(f'{anterior} -> {proximo}', end='')
auxiliar = anterior + proximo
contador2 = 3
while contador2 < contador:
    auxiliar = anterior + proximo
    print(f' -> {auxiliar}', end='')
    anterior = proximo
    proximo = auxiliar
    contador2 += 1

