'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''

from mailbox import MaildirMessage


primeiro_termo = int(input('Primeiro termo: '))
razao_pa = int(input('Razão da PA: '))
termo = primeiro_termo
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo} -> ', end='')
        termo += razao_pa
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))
print('FIM')
print(f'Progressão finalizada com {total} termos mostrados')

#REVER
