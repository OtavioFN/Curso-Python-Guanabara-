# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
name = str(input('Digite seu nome completo: ')).strip()
splited_name = name.split()
print(f'Seu primeiro nome é \033[31m{splited_name[0]}\033[0m')
print(f'Seu último nome é \033[32m{splited_name[-1]}\033[0m')

# 31 - Vermelho
# 32 - Verde

# Ou:

'''name = str(input('Digite seu nome completo: ')).strip()
splited_name = name.split()
print(f'Seu primeiro nome é {splited_name[0]}')
print(f'Seu último nome é {splited_name[len(splited_name)-1]}')'''

