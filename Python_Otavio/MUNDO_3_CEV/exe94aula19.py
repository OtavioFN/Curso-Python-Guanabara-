'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''

sexo = ''
person = dict()
people = list()
resume = ''
ppl = 0
women = list()
age = 0
above_average = list()
media = 0
while True:
    person['nome'] = str(input('Informe o nome da pessoa: '))
    sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()
    while sexo not in 'MF':
        sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()
    person['sexo'] = sexo
    person['idade'] = int(input('Informe a sua idade: '))
    age += person['idade']
    people.append(person.copy())
    person.clear()
    ppl += 1
    resume = str(input('Do you want to continue? [Y/N]: ')).strip().upper()
    while resume not in 'YN':
        resume = str(input('Do you want to continue? [Y/N]: ')).strip().upper()
    if resume == 'N':
        break
media = age/ppl

for i in people:
    if i['sexo'] == 'F':
        women.append(i['nome'])
    if i['idade'] > media:
        above_average.append(i['nome'])

print(f'{ppl} pessoas se cadastraram')
print(f'A média de idade é {media:.0f} anos')
print(f'As mulheres cadastradas foram {women}')
print(f'As pessoas velhinhas são {above_average}')

