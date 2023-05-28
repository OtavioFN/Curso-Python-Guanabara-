'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, 
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

def fatorial(a,show=False):
    '''
    a -> valor a ser calculado
    show -> valor (opcional) que indicará ser o valor será retornado ou não '''
    fat = 1
    for i in range(a,0,-1):
        fat *= i
    if show == False:
        return fat
    elif show == True:
        print(fat)


fatorial(5,True)

fatorial(6)