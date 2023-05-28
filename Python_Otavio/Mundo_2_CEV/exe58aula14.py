'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.'''

'''from random import randint as r
numero = r(0, 10)
palpite = int(input('Adivinhe um número entre 0 e 10: '))
tentativas = 1
while palpite != numero:
    if palpite < numero:
        print('O número sorteado é maior que o número que você chutou!')
        palpite = int(input('Tente novamente, qual é seu palpite?: '))
    else:
        print('O número sorteado é maior que o número que você chutou!')
        palpite = int(input('Tente novamente, qual é seu palpite?: '))
    tentativas += 1
if tentativas == 1:
    print(f'Parabéns, você acertou! Você precisou de somente {tentativas} tentativa')
else:
    print(f'Parabéns, você acertou! Você precisou de somente {tentativas} tentativas')
    '''

from random import randint
computador = randint(0,10)
tentativas = 0
acertou = False
while acertou == False:
    palpite = int(input('Informe um número entre 0 e 10: '))
    tentativas += 1
    if palpite == computador:
        acertou = True
    else:
        if palpite > computador:
            print('Menos... Tente novamente!')
        else:
            print('Mais... Tente novamente!')
print(f'Parabéns, você acertou! Você precisou de {tentativas} tentativas para conseguir.')
