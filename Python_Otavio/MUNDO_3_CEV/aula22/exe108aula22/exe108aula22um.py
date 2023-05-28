'''Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.'''

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

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço}'.replace('.',',')
