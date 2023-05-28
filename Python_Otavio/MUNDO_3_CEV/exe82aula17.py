'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
'''odd_numbers = []
even_numbers = []
numbers = []
while True:
    n = int(input('Type a integer value: '))
    numbers.append(n)
    if n % 2 == 0:
        even_numbers.append(n)
    else:
        odd_numbers.append(n)
    proceed = str(input('Do you want to continue? [Y/N]: ')).strip().upper()
    while proceed not in 'YN':
        proceed = str(input('Do you want to continue? [Y/N]: ')).strip().upper()
    if proceed == 'N':
        break
print(f'The entire list is {numbers}')
print(f"The odd numbers' list is {odd_numbers}")
print(f"The even numbers' list is {even_numbers}")'''

# Guanabara
odd_numbers = []
even_numbers = []
numbers = []
while True:
    n = int(input('Type a integer value: '))
    numbers.append(n)
    proceed = str(input('Do you want to continue? [Y/N]: ')).strip().upper()
    while proceed not in 'YN':
        proceed = str(input('Do you want to continue? [Y/N]: ')).strip().upper()
    if proceed == 'N':
        break

for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)
    else:
        odd_numbers.append(n)

print(f'The entire list is {numbers}')
print(f"The odd numbers' list is {odd_numbers}")
print(f"The even numbers' list is {even_numbers}")