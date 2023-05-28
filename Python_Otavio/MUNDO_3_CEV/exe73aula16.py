'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

teams = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Botafogo', 'América-MG', 'Fortaleza', 'São Paulo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Coritiba', 'Cuiabá', 'Avaí', 'Atlético-GO', 'Ceará SC', 'Juventude')

print(f'The top five teams are: ', end='')
for i in teams[:5]:
    print(f'{i}, ', end='')
print('')
print('=-'*20)
print(f'The last four teams are: ', end='')
for i in teams[-4:]:
    print(f'{i}, ', end='')
print('')
print('=-'*20)
print(f'The teams listed in alphabetic order get like this: ', end='')
for i in sorted(teams):
    print(f'{i}, ', end='')
print('')
print('=-'*20)
print(f'Corinthians is in {teams.index("Corinthians")}ª position')

