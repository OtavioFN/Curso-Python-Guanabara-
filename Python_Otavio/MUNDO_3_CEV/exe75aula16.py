'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

e1 = int(input('Type the first number of the tuple: '))
e2 = int(input('Type the second number of the tuple: '))
e3 = int(input('Type the third number of the tuple: '))
e4 = int(input('Type the fourth number of the tuple: '))
numbers = (e1,e2,e3,e4)
if 9 in numbers:
    print(f'The number 9 appeared {numbers.count(9)} times')
else:
    print("Number 9 didn't appear in tuple")
if 3 in numbers:
    print(f'The number 3 has appeared in {numbers.index(3)+1}º position')
else:
    print("Number 3 didn't appear in tuple")
print('The even numbers are: ', end='')
for n in numbers:
    if n % 2 == 0:
        print(n,end=' ')