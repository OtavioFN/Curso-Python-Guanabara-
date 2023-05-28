'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

def aumentar(a=0 ,b=0):
    aumento = (a/100 * b) + b
    return aumento

def diminuir(a=0,b=0):
    subtracao = (a/100 * b) + b
    return subtracao

def dobro(a):
    return a * 2

def metade(a):
    return a / 2


    
