# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('='*25)
print('   10 TERMOS DE UMA PA')
print('='*25)
pt = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
dc_tm = pt + 10 * rz # Fórmula para conseguir o décimo termo de uma PA 
for i in range(pt, dc_tm , rz):
    print(f'{i} -> ', end='')
print('ACABOU')

#REVER
# OU -----------

#Meu jeito

pt = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
for i in range(0,10):
    print(f'{pt}', end=' -> ')
    pt += rz
print('Acabou')