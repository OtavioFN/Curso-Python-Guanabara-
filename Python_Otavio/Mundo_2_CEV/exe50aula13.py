# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0 
cont = 0
contp = 0
for i in range(6):
    num = int(input('Informe um número inteiro: '))
    if num % 2 == 0:
        soma += num
        contp += 1
        cont += 1
    else:
        cont += 1
print(f'Dentre os {cont} números que você informou, a soma dos {contp} números pares resulta em {soma}')
