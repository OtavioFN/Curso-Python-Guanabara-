#nome = str(input('Digite seu nome: ')).strip()
'''name = 'Cláudio Buchecha Damariz'
splited_name = name.split(' ', 1)
first_name = splited_name[0]
surnames = ' '.join(splited_name[1:])
print(first_name)
print(surnames)'''


# EMAIL INSTITUCIONAL
'''from random import randint
name1 = str(input('Digite seu nome completo: ')).strip().lower() 
name = name1.replace(' das ', ' ').replace(' dos ',' ').replace(' da ',' ').replace(' de ', ' ').replace(' do ', ' ')
name_spl = name.split()
sufixo = '@aluno.ifal.edu.br'
randomnumber = str(randint(1,20))
iniciais = ''
for n in name_spl:
    iniciais = iniciais + n[0]
email = iniciais + randomnumber + sufixo
print(email)'''

'''from random import randint
name = str(input('Digite seu nome completo: ')).lower().strip()
name = name.replace(' das ', ' ').replace(' dos ', ' ').replace(' da ', ' ').replace(' de ', ' ').replace(' do ', ' ')
splitted_name = name.split()
ending = '@aluno.ifal.edu.br'
number = str(randint(1, 20))
initial = ''
for n in splitted_name:
  initial = initial + n[0]
email = initial + number + ending
print(email)'''

'''tempo = int(input('Digite quantos anos tem seu carro?: '))
if tempo <= 3:
  print('Seu carro já está velho!')
else:
  print('Seu carro é novo!')'''

from math import ceil


print(ceil(9.1))
