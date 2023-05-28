'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, 
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

somaidade = 0
maior_idadehomem = 0
nome_homemmaisvelho = ''
mulheresmaisnovas = 0
for i in range(1,5):
    print(f'--- Pessoa {i} ---')
    nome = str(input('Informe seu nome: ')).strip()
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Informe seu sexo: (M/F) ')).strip().upper()
    somaidade += idade
    if sexo == "M" and idade > maior_idadehomem:
    # ou sexo in "Mm"
        nome_homemmaisvelho = nome
        maior_idadehomem = idade
    if idade < 20 and sexo == "F":
        mulheresmaisnovas += 1
    
mediaidade = somaidade / 4
print(f'''A média de idade do grupo é de {mediaidade} anos!
O nome do homem mais velho é {nome_homemmaisvelho} e ele tem {maior_idadehomem} anos!
Existem {mulheresmaisnovas} mulheres mais novas que 20 anos!''')