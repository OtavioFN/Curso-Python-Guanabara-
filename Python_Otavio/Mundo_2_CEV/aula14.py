# Estrutura de repetição com teste lógico: WHILE

'''c = 1 
while c != 10:
    print(c)
    c += 1
print('Acabou')'''

'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')'''

n = 1
pares = 0
impares = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            pares += 1
        elif n % 2 == 1:
            impares += 1
print(f'Houveram {pares} números pares e {impares} números ímpares')