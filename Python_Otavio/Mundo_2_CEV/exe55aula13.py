'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

maiorpeso = 0
menorpeso = 0
for i in range(1,6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    if i == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        elif peso < menorpeso:
            menorpeso = peso
print(f'''O maior peso foi de {maiorpeso}kg
O menor peso é foi de {menorpeso}kg''')