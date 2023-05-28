'''fator = int(input('Informe o número o qual deseja saber o fatorial: '))
fatorial = 1
for i in range(fator, 0,-1):
    fatorial *= i

print(f'O fatorial de {fator} é {fatorial}')'''

'''from random import randint
for j in range(10):
    aposta = []
    for i in range(6):
        dezena = randint(1,60)
        aposta.append(dezena)
    print(aposta)'''

'''a = 0
if a <= 0:
    print('O valor de a é menor ou igual a zero')
elif a == 0:
    print('O valor de a é igual a zero')'''

'''print('*** CÁLCULO DO IAC ***')
cq = float(input('Informe a medida de circunferência do seu quadril: '))
altura = float(input('Informe a medida da sua altura em metros: '))

iac = cq / (altura * altura ** 0.5) - 18
print(iac)

if iac >= 30:
    print('Excesso de gordura')
elif iac >= 26:
    print('Moderada')
elif iac >= 20:
    print('Ideal')
elif iac>= 16:
    print('Baixa')
elif iac >= 10:
    print('Excepcionalmente baixa')'''

'''maioridade = 0
menoridade = 0
dmaior = 0 
dmenor = 0
tot_idade = 0
for i in range(5):
    idade = int(input(f'Informe a idade da {i+1}º pessoa: '))
    tot_idade += idade
    if i == 0:
        maioridade = idade
        menoridade = idade
    elif idade > maioridade:
        maioridade = idade
    elif idade < menoridade:
        menoridade = idade
    if idade >= 18:
        dmaior += 1
    else:
        dmenor += 1
media = tot_idade / 5'''
#print(f'''Maior idade: {maioridade}
#Menor idade: {menoridade}
#{dmaior} pessoas com mais de 18 anos
#{dmenor} pessoas com menos de 18 anos
#A média de idade é {media}''')

'''from contextlib import ContextDecorator


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
    mais = int(input('Quantos termos você deseja ver a mais?: '))
print('FIM')
print(f'Você realizou a operação utilizando {total} termos!')'''

'''a = 1/0
print(a)
    
b = 0%2
print(b)'''

n = 'ameixa'
if 'aeiou' in n[0] :
    print('aaaa')

n = [0,1,2,4,2,2,2]
print(n.index(2))