'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

aluno = dict()
aluno['nome'] = str(input('Informe o nome do aluno: '))
aluno['media'] = float(input('Informe a média do aluno: '))
if aluno['media'] < 7 and aluno['media'] >= 6:
    print(f'O aluno(a) {aluno["nome"]} está de RECUPERAÇÃO')
elif aluno['media'] < 6:
    print(f'O aluno(a) {aluno["nome"]} está REPROVADO')
else:
    print(f'O aluno(a) {aluno["nome"]} está APROVADO!')
