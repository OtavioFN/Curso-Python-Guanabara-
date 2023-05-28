# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
name = str(input('Digite seu nome completo: ')).strip()
if "silva" in name.lower() == True:
    print(f'Seu nome tem Silva? \033[33m{"silva" in name.lower()}\033[0m')
else:
    print(f'Seu nome tem Silva? \033[31m{"silva" in name.lower()}\033[0m')