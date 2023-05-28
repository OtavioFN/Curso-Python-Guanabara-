'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

from socket import SOMAXCONN


contador = 0
soma = 0
numero = 0
while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero != 999:
        soma += numero
    else:
        break
    contador += 1
print(f'Você digitou {contador} números e a soma entre eles resulta em {soma}')