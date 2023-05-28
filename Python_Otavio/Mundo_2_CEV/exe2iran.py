'''Crie um programa que solicite uma senha do

usuário e verifique se:

1. A senha possui ao menos uma letra minúscula

2. A senha possui ao menos uma letra maiúscula

3. A senha possui ao menos um numeral

▸ Dica: percorra a string e verifique se cada caractere está no intervalo
correspondente às maiúsculas, minúsculas ou numerais (ex.: letra >= 'a')
and letra <= ‘z')'''

letra_maiuscula = False
letra_minuscula = False
numeral = False
senha = str(input('Informe sua senha: '))

'''for i in senha:
    if i == i.upper():
        letra_maiuscula = True
    if i == i.lower():
        letra_minuscula = True
    if i >= '0' and i <= '9':
        numeral = True
if letra_maiuscula == True:
    print('A senha possui pelo menos uma letra minúscula')
else:
    print('A letra não possui letras maiúsculas!')
if letra_minuscula == True:
    print('A senha possui pelo menos uma letra minúscula!')
else:
    print('A senha não possui nenhuma letra minúscula!')
if numeral == True:
    print('A senha possui pelo menos um numeral!')
else:
    print('A senha não possui nenhum numeral!')'''

#TABELA ASCII

for i in senha:
    if i >= 'A' and i <= 'Z':
        letra_maiuscula = True
    if i >= 'a' and i <= 'z':
        letra_minuscula = True
    if i >= '0' and i <= '9':
        numeral = True
if letra_maiuscula == True:
    print('A senha possui pelo menos uma letra minúscula')
else:
    print('A letra não possui letras maiúsculas!')
if letra_minuscula == True:
    print('A senha possui pelo menos uma letra minúscula!')
else:
    print('A senha não possui nenhuma letra minúscula!')
if numeral == True:
    print('A senha possui pelo menos um numeral!')
else:
    print('A senha não possui nenhum numeral!')
