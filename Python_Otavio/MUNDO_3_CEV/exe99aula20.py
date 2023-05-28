'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
def maior(* num):
    cont = 0
    highest = 0
    for index,number in enumerate(num):
        if index == 0 or number > highest:
            highest = number
    print(f'Dentre todos os valores, {highest} é o maior entre eles!')


valores = [1,2,3,4,4,5]
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()