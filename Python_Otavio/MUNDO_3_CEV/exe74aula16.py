"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""
'''from random import randint
number_one = randint(0,9)
number_two = randint(0,9)
number_three = randint(0,9)
number_four = randint(0,9)
number_five = randint(0,9)
highest_number = number_one
lowest_number = number_one
if lowest_number > number_two:
    lowest_number = number_two
if highest_number < number_two:
    highest_number = number_two
if lowest_number > number_three:
    lowest_number = number_three
if highest_number < number_three:
    highest_number = number_three
if lowest_number > number_four:
    lowest_number = number_four
if highest_number < number_four:
    highest_number = number_four
if lowest_number > number_five:
    lowest_number = number_five
if highest_number < number_five:
    highest_number = number_five

numbers = (number_one, number_two, number_three, number_four, number_five)
print(numbers)
print(f'The highest number is {highest_number}')
print(f'The lowest number is {lowest_number}')'''

'''from random import randint
number_one = randint(1,10)
number_two = randint(1,10)
number_three = randint(1,10)
number_four = randint(1,10)
number_five = randint(1,10)
highest_number = 0
lowest_number = 0

numbers = (number_one, number_two, number_three, number_four, number_five)
for pos, i in enumerate(numbers):
    if pos == 1:
        highest_number = i
        lowest_number = i
    if highest_number < i:
        highest_number = i
    if lowest_number > i:
        lowest_number = i
print(numbers)
print(f'The highest number is {highest_number}')
print(f'The lowest number is {lowest_number}')'''

'''# Guanabara

from random import randint

numbers = (randint(1,10), randint(1,10), randint(1,10), randint(1,10),randint(1,10))
print('The sorted numbers were: ', end='')
for n in numbers:
    print(f'{n} ', end='')
print(f'\nThe highest number is {max(numbers)}')
print(f'The lowest number is {min(numbers)}')'''
