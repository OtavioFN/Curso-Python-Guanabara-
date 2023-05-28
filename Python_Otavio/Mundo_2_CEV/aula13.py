#Estrutura de repetição com variável de controle : for

'''for c in range(1,6): # Repetirá 5 vezes
    print('Oi')
print('Fim') # Fora do for

for c in range(0,6): #Repetirá 6 vezes
    print('Oi')
    print('Fim') # Dentro do for

for c in range(0,6): # Retornará de 0 até 5, pois o último ele ignora
    print(c)

for c in range(6, 0,-1): # Conta de trás pra frente
    print(c)
print('Fim')

for c in range(0,7,2): # Conta de 0 a 6 pulando 2 números
    print(c)'''

'''n = int(input('Digite um número: '))
for c in range(0, n):
    print(c)
print('FIM') # Conta de 0 ao número anterior ao que eu escolhi, pois ele ignora o meu

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('Fim') # Agora sim ele vai até o número que eu digitei
'''
'''Início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for c in range(Início, fim+1, passo): # Eu que digitei os valores da range
    print(c)'''

# Somatório
'''s = 0
for c in range(0,3):
    n = int(input('Digite um valor: '))
    s += n
print(f'Somatório: {s}')
print('Fim')'''
'''for i in range(1,11):
    print('Olá, Mundo!')'''

'''ifal = 'Instituto Federal de Alagoas'
for i in ifal:
    print(i)'''


from unittest import result
dias = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
for dia in dias:
    print(dia)
    if dia == 'sexta':
        print('Sextou!')

for i in range(11):  # A variável (i) vai receber cada valor de uma sequência de 0 à 9
    for j in range(i):  # Para cada repetição eu defino uma outra repetição que faz com que a variável (j) vá de 0 à uma sequência que termine em (i)
        print('*', end='')  # O end indica o que virá após a string
    print()  # como o end não pula linha, eu preciso de um print para pular uma linha a cada repetição, por isso o print vazio

# usei dois for para uma instrução: um for vai de 0 até 10 (9 no caso) e outro que vai de
# cada linha desse programa é controlada pelo for interno (for j)
# e o fato de eu imprimir 4 *'s e depois 5 se dá pelo for externo (for i)

'''tab = int(input('Informe um número para realizarmos a sua tabuada: '))
print(f'Tabuada do {tab} !!!')
for numero in range(11):
    print(f' {tab} x {numero} = {tab*numero}')'''

'''for tabuada in range(11):
    print(f'Tabuada do {tabuada}')
    for numero in range(11):
        print(f'{tabuada} x {numero} = {tabuada*numero}')

for i in reversed(range(11)): # A função reversed inverte a ordem dos elementos em uma sequência ou lista
    print(i)

from random import randint

for i in range(10):
    aposta = []
    for j in range(6):
        dezena = randint(1,60)
        aposta.append(dezena)
    print(aposta)'''

fatorial = 1
num = int(input('Informe o número que deseja saber o fatorial: '))
for i in range(num, 0, -1):
    fatorial *= i
print(fatorial)