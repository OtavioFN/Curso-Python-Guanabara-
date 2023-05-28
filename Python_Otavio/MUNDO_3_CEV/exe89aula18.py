'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''


data = []
students = []

while True:
    data.append(str(input('Digite o nome do estudante: ')))
    data.append(float(input(f'Informe a primeira nota de {data[0]}: ')))
    data.append(float(input(f'Informe a segunda nota de {data[0]}: ')))
    students.append(data[:])
    data.clear()
    resume = str(input('Do you want to continue? [Y/N]: ')).strip().upper()
    while resume not in 'YN':
        resume = str(input('Do you want to continue? [Y/N]: ')).strip().upper()
    if resume == 'N':
        break

print('No.   Name      Medial')
for num,stu in enumerate(students):
    media = (stu[1] + stu[2])/2
    print(f'{num:^5}{stu[0]:^10}{media:^5}')

while True:
    number = int(input("Tell the students' position u want to know the grades: "))
    print(f'As notas de {students[number][0]} foram {students[number][1]:.1f} e {students[number][2]:.1f}')
    resume = str(input('Dou you want to continue? [Y/N]: ')).strip().upper()
    while resume not in 'YN':
        resume = str(input('Dou you want to continue? [Y/N]: ')).strip().upper()
    if resume == 'N':
        break    
