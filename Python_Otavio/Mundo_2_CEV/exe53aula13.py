'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:'''

#REVER PROGRAMAAAAAAAAA

'''frase = str(input('Digite a frase a ser analisada: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, 0, -1):
    inverso += junto[letra]
if inverso  == junto:
    print('A frase é o palíndromo')
else:
    print('A frase não é um palíndromo')'''

# OUUU

frase = str(input('Digite a frase a ser analisada: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1] # Inverso da string
if inverso  == junto:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')

# REVER EXERCÍCIO FUTURAMENTE
