'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

words = ('Learn', 'Program', 'Language', 'Python', 'Course', 'Free', 'Practice', 'Work', 'Market', 'Programmer', 'Future')
for w in words:
    print(f'\nIn the word {w} we have the vocals: ', end = '')
    for lt in w:
        if lt.lower() in 'aeiou':
            print(f'{lt} ',end='')

