nome = str(input('Qual é o seu nome: '))
if nome == 'Otávio':
    print('Que nome bonito!') # Condição Simples - Somente o if
elif nome == 'Naruto' or nome == 'Goku':
    print('Seu nome é bem popular!') # Estrutura condicional aninhada - Uso do if com o elif, tendo o else ou não.
elif nome in 'Ester Fernandes de Souza' or nome in 'Kaline Fernandes de Oliveira':
    print('Belo nome feminino!')
else: 
    print('Seu nome é bem normal.') # Estrutura condicional composta - O if mais o elif/else
print(f'Tenha uma boa noite, {nome}!')

# OBS: Iran Apresenta módulo datetime

import datetime
hoje = datetime.datetime.today() # Função que retorna dados do dia atual
print(hoje)
dia_da_semana = hoje.weekday() # Retorna o dia da semana atual

# OBS: TODA FUNÇÃO TEM QUE TER PARÊNTESES

# Os dias da semana se apresentam de 0 a 6, sendo segunda-feira == 0 e domingo == 6

if dia_da_semana == 0:
    dia_da_semana = 'segunda-feira'
elif dia_da_semana == 1:
    dia_da_semana = 'terça-feira'
elif dia_da_semana == 2:
    dia_da_semana = 'quarta-feira'
elif dia_da_semana == 3:
    dia_da_semana = 'quinta-feira'
elif dia_da_semana == 4:
        dia_da_semana = 'sexta-feira'
elif dia_da_semana == 5:
    dia_da_semana = 'sábado'
else:
    dia_da_semana = 'domingo'

print(f'Hoje é {dia_da_semana}!')