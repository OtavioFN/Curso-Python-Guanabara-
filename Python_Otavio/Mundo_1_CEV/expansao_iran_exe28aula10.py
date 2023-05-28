import random as r

numero = r.randint(1, 100)
numero_chutado = 0
limite_inferior = 1
limite_superior = 100
jogo_encerrado = False
while jogo_encerrado == False:
    numero_chutado = int(input(f'Digite um número entre {limite_inferior} e {limite_superior}: '))
    print('Verificando resposta...')
    if numero_chutado == numero:
        print('Parabéns, você acertou!')
        jogo_encerrado = True
    else:
        if numero_chutado < numero:
            print('Você errou! Tente novamente!')
            limite_inferior = numero_chutado + 1
        else:
            print('Você errou! Tente novamente!')
            limite_superior = numero_chutado - 1
        if limite_inferior == limite_superior:
            print('Você perdeu pois foi imprensado')
            jogo_encerrado = True
'''else:
    #print(f'Que pena, você errou! O número sorteado foi {numero}, e não {numero_chutado} !')
#EXPANSÃO IRAN---
    if numero_chutado < numero:
        print(f'Que pena, o número sorteado é maior que {numero_chutado}')
        print('Vamos tentar novamente?')
        numero_chutado = int(input(f'Digite um número entre {numero_chutado+1} a 10: '))
    
    else:
        print(f'Que pena, o número sorteado é menor que {numero_chutado}')
        print('Vamos tentar novamente?')
        numero_chutado = int(input(f'Digite um número entre 1 a {numero_chutado-1}: '))
    if numero == numero_chutado:
        print('Você acertou!')
    else:
        print('Você errou!')'''
