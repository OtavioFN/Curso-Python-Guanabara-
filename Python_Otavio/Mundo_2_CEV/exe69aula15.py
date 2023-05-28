'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

maior_de_18 = 0
homens = 0
mulheres_menos_20anos=0
while True:
    print('='*20)
    print('CADASTRE UMA PESSOA')
    print('='*20)
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()
    idade = int(input('Informe sua idade: '))
    if idade > 18:
        maior_de_18 += 1
    elif sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres_menos_20anos += 1
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break

print('Programa encerrado!')
if maior_de_18 == 0:
    print('Não houve maiores de idade!')
elif maior_de_18 == 1:
    print('Houve somente um maior de idade!')
else:
    print(f'Houve {maior_de_18} maiores de idade!')

if homens == 0:
    print('Não houve homens cadastrados!')
elif homens == 1:
    print('Houve somente um homem cadastrado!')
else:
    print(f'Houve {homens} homens cadastrados!')
if mulheres_menos_20anos == 0:
    print('Não houve nenhuma mulher com menos de 20 anos cadastrada!')
elif mulheres_menos_20anos == 1:
    print('Somente uma mulher com menos de 20 anos foi cadastrada!')    
else:
    print(f'Houve {mulheres_menos_20anos} mulheres com menos de 20 anos cadastradas!')
