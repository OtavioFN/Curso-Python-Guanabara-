'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

print('GERADOR DE PA')
print('-=' * 10)

primeiro_termo = int(input('Primeiro termo: '))
razao_pa = int(input('Razão da PA: '))
termo = primeiro_termo
contador = 0
while contador != 10:
    print(f'{termo} -> ', end='')
    termo += razao_pa
    contador += 1
print('FIM')

'''primeiro_termo = int(input('Primeiro termo: '))
razao_pa = int(input('Razão da PA: '))
for i in range(1,11):
    print(f'{primeiro_termo} -> ', end='')
    primeiro_termo += razao_pa
print('FIM')'''