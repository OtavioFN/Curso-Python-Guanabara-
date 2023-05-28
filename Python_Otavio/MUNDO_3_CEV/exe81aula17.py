'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disto, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

numbers = []
while True:
    n = int(input('Type a value: '))
    numbers.append(n)
    proceed = str(input('Do you want to continue? [Y/N]: ')).strip().upper()
    while proceed not in 'YN':
        proceed = str(input('Do you want to continue? [Y/N]: ')).strip().upper()
    if proceed[0] == 'N':
        print('Programa encerrado!')
        break
print(f'The list has about {len(numbers)} elements')
numbers.sort(reverse=True)
print(f'The reverse ordened list is {numbers}')
if 5 in numbers:
    print("There's 5 in the list")
else:
    print("There isn't any 5 in the list")