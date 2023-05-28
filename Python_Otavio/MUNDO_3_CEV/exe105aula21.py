'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)'''

def notas(* notas,sit=False):
    '''
    notas -> informe as notas
    sit -> Informe com um valor booleano se você deseja que a função retorne ou não a situação'''
    aluno = dict()
    soma = 0 
    quantity = 0
    highest = 0
    lowest = 0
    for num,nota in enumerate(notas):
        if num == 0 or nota > highest:
            highest = nota
        if num == 0 or nota < lowest:
            lowest = nota
        quantity += 1
        soma += nota
    medium = soma/len(notas)
    aluno['Quantidade de notas: '] = quantity
    aluno['A maior nota: '] = highest
    aluno['A menor nota: '] = lowest
    aluno['A média da turma: '] = medium
    if sit == True:
        if medium >= 6:
            aluno['Situação: '] = 'Aprovados!'
        else:
            aluno['Situação: '] = 'Reprovados!'
        return aluno
    else:
        return aluno

print(notas(1,2,4,5,6,6,22,1,1,sit=True))

# Guanabara

def notas(*n,sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'RUIM'
    return r

#Programa Principal
resp = notas(5.5,2.5,1,5,sit = True)
print(resp)
help(notas)