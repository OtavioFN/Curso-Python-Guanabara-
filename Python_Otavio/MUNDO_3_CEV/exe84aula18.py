'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''


'''quantity_registered = 0
most_heavy = 0
most_thin = 0
most_heavy_ppl = []
most_thin_ppl = []
people = []
data = []
next = ''

while True:
    data.append(str(input('Digiite seu nome: ')))
    data.append(int(input('Informe seu peso em KG: ')))
    if quantity_registered == 0 or most_heavy < data[1]:
        most_heavy = data[1]
    if quantity_registered == 0 or most_thin > data[1]:
        most_thin = data[1]
    people.append(data[:])
    data.clear()
    quantity_registered += 1
    resume = str(input('Do u want to continue? [Y/N]: ')).strip().upper()
    while resume[0] not in 'YN':
        resume = str(input('Do u want to continue? [Y/N]: ')).strip().upper()
    if resume == 'N':
        break

for p in people:
    if p[1] == most_heavy:
        most_heavy_ppl.append(p[0])
    if p[1] == most_thin:
        most_thin_ppl.append(p[0])

print(f'Foram cadastradas {quantity_registered} pessoas')
print(f'As mais leves são {most_thin_ppl}, que pesam {most_thin}KG')
print(f'As mais pesadas são {most_heavy_ppl}, que pesam {most_heavy}KG')
'''

'''

# GUANABARA

temp = []
prin = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]: ')
    if resp in 'Nn':
        break
print('-=" * 30)
print(f'Ao todo, você cadastrou  {len(princ)} pessoas')
print(f'O maior peso foi de {mai}Kg. Peso de ',end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]] ',end='')
    if p[1] == men:
        print(f'[{p[0]] ',end='')
print()
        '''
