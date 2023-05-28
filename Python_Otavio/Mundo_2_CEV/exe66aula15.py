'''Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

numero = soma = contador = 0
while True:
    numero = int(input('Informe um número: '))
    if numero == 999:
        break
    else:
        soma += numero
        contador += 1
print(f'Foram digitados {contador} números, e a soma entre eles resulta em {soma}')
