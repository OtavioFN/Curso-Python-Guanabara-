#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opçao = int(input('Informe a opção desejada: '))
if opçao == 1: 
    print(f'O número {n} convertido para binário é igual a {bin(n)[2:]}')
elif opçao == 2:
    print(f'O número {n} convertido para octal é igual a {oct(n)[2:]}')
elif opçao == 3:
    print(f'O número {n} convertido para hexadecimal é igual a {hex(n)[2:]}')
else:
    print('Opção Inválida!')
