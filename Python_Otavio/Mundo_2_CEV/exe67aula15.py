'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.'''

while True:
    print('-'*20)
    numero = int(input('Informe o número: '))
    print('-'*20)
    if numero < 0:
        break
    else:
        for i in range(1,11):
            print(f'{numero} x {i} = {numero*i}')
print('PROGRAMA ENCERRADO!')