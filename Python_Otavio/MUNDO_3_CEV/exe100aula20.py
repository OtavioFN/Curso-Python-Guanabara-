'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''

from random import randint

def sorteia(lista):
    for num in range(5):
        lista.append(randint(1,10))
    print(lista)

def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'A soma de todos os números pares da lista resulta em {soma}') 

numeros = list()
sorteia(numeros)
somaPar(numeros)

