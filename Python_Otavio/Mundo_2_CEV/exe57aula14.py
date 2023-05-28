'''Faça um programa que leia o sexo de uma pessoa, 
mas só aceite os valores 'M' ou 'F'. Caso esteja errado, 
peça a digitação novamente até ter um valor correto.'''

'''sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inváliados. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')'''

sexo = str(input('Informe sua sexualidade: [M/F] ')).upper()
while sexo not in 'MF':
    print('Digite novamente!')
    sexo = str(input('Informe seu sexo: ')).upper()
print(f'Sexo {sexo} registrado com sucesso')




