'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''
print('-='*20)
print('Analisador de triângulos...')
print('-='*20)

reta1 = float(input('Digite o comprimento da primeira reta em centímetros: '))
reta2 = float(input('Digite o comprimento da segunda reta em centímetros: '))
reta3 = float(input('Digite o comprimento da terceira reta em centímetros: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('As três retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')