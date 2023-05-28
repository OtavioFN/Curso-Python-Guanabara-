'''Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''

fatorial = int(input('Informe o número o qual deseja saber o fatorial: '))
numero = fatorial
fat = 1
print(f'Calculando {fatorial}! = ',end='')
while fatorial >= 1:
    print(f'{numero}', end='')
    numero -= 1
    if numero >= 1:
        print(' x ', end ='')
    else: 
        print(' = ', end='')
    fat *= fatorial
    fatorial -= 1
print(f'{fat}')

'''fatorial = int(input('Informe o número o qual deseja saber o fatorial: '))
fat = fatorial
print(f'Calculando o fatorial de {fat}! = {fat} x ',end='')
for i in range(fatorial-1, 0, -1):
    fatorial *= i
    fat -= 1
    if fat > 1:
        print(f'{fat} x ', end='')
    else:
        print(f'{fat} = ',end = '')
print(fatorial)

# Usando o FOR
'''
