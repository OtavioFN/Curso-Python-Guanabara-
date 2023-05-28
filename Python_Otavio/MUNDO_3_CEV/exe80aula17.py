'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

'''
'''list = []
for c in range(0, 5):
    n = int(input('Type a value: '))
    if c == 0 or n > list[-1]:
        list.append(n)
    else:
        pos = 0
        while pos < len(list):
            if n <= list[pos]:
                list.insert(pos, n)
                break
            pos += 1
print(f'Os valores digitados foram {list}')'''

numbers = []
for num in range(5):
    n = int(input('Type a value: '))
    if num == 0:
        numbers.append(n)
        print('Adicionado no começo da lista')
    elif n > numbers[-1]:
        numbers.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(numbers):
            if n <= numbers[pos]:
                numbers.insert(pos, n)
                print(f'Adicionado à posição {pos} da lista')
                break
            pos += 1
            
print(numbers)
# REVER