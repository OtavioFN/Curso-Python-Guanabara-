'''A Sequência de Fibonacci consiste numa
sucessão infinita de números que obedecem
um padrão em que cada elemento subsequente
é a soma dos dois anteriores: 1, 1, 2, 3, 5, 8, 13...

▸ A espiral de Fibonacci aparece quando construímos
uma série de quadrados cujos lados são os números
da sequência de Fibonacci. Essa espiral está presente em diversas formas da natureza,
desde conchas de caramujos até em algumas galáxias. A sequência também é objeto
de estudo de várias áreas, tendo aplicações até no mercado de ações.

▸ Assim, construa um programa que imprima os 20 primeiros números dessa sequência.'''

ant = 1
prox = 1
for i in range(20):
    '''print(ant)
    aux = ant
    ant = prox
    prox += aux'''
    ant, prox = prox, ant + prox