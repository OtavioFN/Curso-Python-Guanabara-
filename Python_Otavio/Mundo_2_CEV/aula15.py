# Instrução break e loopings infinitos

'''
LOOPING FINITO

contador = 1
while contador <= 10:
    print(f'{contador}', end=' -> ')
    contador +=1
print('Acabou')'''

'''
LOOPING INFINITO

contador = 1    
while True:
    print(f'{contador}', end=' -> ')
    contador +=1
print('Acabou')'''

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    else:
        s += n
print(f'A soma vale {s}')