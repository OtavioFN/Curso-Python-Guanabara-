'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

from tkinter import N
from xmlrpc.client import boolean


contador = 1
continuar = ''
fim = False
numero = int(input('Digite um número: '))
maior_valor = numero
menor_valor = numero
soma = numero
while not fim:
    if numero > maior_valor:
        maior_valor = numero
    if numero < menor_valor:
        menor_valor = numero

    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continuar == 'S':
        contador += 1
        soma += numero
        numero = int(input('Digite um número: '))
    elif continuar == 'N':
        fim = True
    else:
        print('Digite uma resposta válida!')
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
print(f'Você digitou {contador} números e a média foi {soma/contador}')
print(f'O maior valor foi {maior_valor} e o menor foi {menor_valor}') 

# Minha resposta

resposta = 'S'
soma = 0
quantidade = 0
media = 0
maior = 0 
menor = 0
while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()
media = soma/quantidade
print(f'Você digitou {quantidade} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')

# Guanabara
