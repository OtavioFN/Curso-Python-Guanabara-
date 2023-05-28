'''Crie um programa que pergunte a quantidade de alunos de uma turma, para

em seguida ler a nota de cada aluno e, no final, informar:

▸ A menor nota

▸ A maior nota

▸ A média das notas

▸ Quantas notas foram abaixo de 6,0

▸ Quantas notas foram maiores ou iguais a 6,0'''


maiornota = 0
menornota = 0
medianotas = 0
reprovados = 0
aprovados = 0
total_notas = 0
alunos = int(input('Informe quantos alunos a turma possui: '))
for i in range(alunos):
    nota = float(input(f'Informe a nota do {i+1}º aluno: '))
    total_notas += nota
    if i == 1:
        maiornota = nota
        menornota = nota
    if nota > maiornota:
        maiornota = nota
    if nota < menornota:
        menornota = nota
    if nota < 6:
        reprovados += 1
    else:
        aprovados += 1
media = total_notas / alunos
print(f'''A menor nota foi {menornota:.1f}
A maior nota foi {maiornota:.1f}
A média das notas foi {media:.1f}
No total, houveram {reprovados} reprovados e {aprovados} aprovados.''')
