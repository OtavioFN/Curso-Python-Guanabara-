'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

Ex: 
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~
Olá, Mundo!
~~~~~~~~~'''

def escreva(palavra):
    lent = len(palavra) + 4
    print('~' * lent)
    print(f'  {palavra}')
    print('~' * lent)

escreva('Olá, mundo!')
