'''Reescreva a função leiaInt() que fizemos no desafio 104, 
incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

import colorama
colorama.init()


def leiaInt(ask):
    while True:
        try:
            num = int(input(ask))
        except (ValueError,TypeError):
            print('Esse número é inválido')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar um número')
            return 0
        else:
            return num
        
def leiaFloat(ask):
    global num
    while True:
        try:
            num = float(input(ask))
        except (TypeError,ValueError):
            print('Por favor, informe um valor real válido')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não informar nenhum número!')
            return 0 
        else:
            return num


inteiro = leiaInt('Digite um valor inteiro: ')
real = leiaFloat('Digite um valor real: ') 
print(f'O valor inteiro foi {inteiro} e o real foi {real}')
