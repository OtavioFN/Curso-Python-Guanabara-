'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
'''numbers = []
highest_number = 0
lowest_number = 0
pos_highest_number = []
pos_lowest_number = []
for i in range(5):
    n1 = int(input(f'Type a number to ocupe the position {i}: '))
    numbers.append(n1)
print(numbers)

for pos,n in enumerate(numbers):
    if pos == 0 or highest_number < n:
        highest_number = n
    if pos == 0 or n < lowest_number:
        lowest_number = n

for pos,num in enumerate(numbers):
    if num == highest_number:
        pos_highest_number.append(numbers.index(num, pos))
    if num == lowest_number:
        pos_lowest_number.append(numbers.index(num, pos))
if len(pos_highest_number) > 1:
    print(f'The highest number typed was {highest_number} in positions ', end='')
else:
    print(f'The highest number typed was {highest_number} in position ', end='')
for p in pos_highest_number:
    print(f'{p}... ', end='')
if len(pos_lowest_number) > 1:
    print(f'\nThe lowest number typed was {lowest_number} in positions ', end='')
else:
    print(f'\nThe lowest number typed was {lowest_number} in position ', end='')
for p in pos_lowest_number:
    print(f'{p}... ', end='')
'''

numeros = []
maior_numero = 0
menor_numero = 0
posicoes_maior_numero = []
posicoes_menor_numero = []
for i in range(5):
    numeros.append(int(input(f'Informe um número para a posição {i}: ')))
for pos,i in enumerate(numeros):
    if pos == 0 or i > maior_numero:
        maior_numero = i
    if pos == 0 or i < menor_numero:
        menor_numero = i
for pos,i in enumerate(numeros):
    if i == maior_numero:
        posicoes_maior_numero.append(numeros.index(i, pos))
    if i == menor_numero:
        posicoes_menor_numero.append(numeros.index(i, pos))
print(f'O maior número foi {maior_numero} e apareceu nas posições ', end='')
for i in posicoes_maior_numero:
    print(f'{i}... ', end='')
print(f'\nO menor número foi {menor_numero} e apareceu nas posições ', end='')
for i in posicoes_menor_numero:
    print(f'{i}... ', end='')

# Guanabara

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()