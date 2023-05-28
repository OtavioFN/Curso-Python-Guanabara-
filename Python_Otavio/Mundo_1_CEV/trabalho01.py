qa = int(input('Informe a quantidade de alunos da turma: '))
menos6 = 0
maior = 0
menor = 0
soma = 0
mais6 = 0
for i in range(qa):
  nota = float(input(f'Aluno #{i + 1}, informe a nota: '))
  if nota >= 6:
    mais6 += 1
  else:
    menos6 += 1
  soma += nota
  if nota > maior:
    maior = nota
  if nota < menor:
    menor = nota
print(f'Maior nota: {maior}')
print(f'Menor nota: {menor}')
print('Média das notas: {:.2f}'.format((soma / qa)))
print(f'{mais6} alunos com nota maior que 6\n{menos6} alunos com nota menor que 6')