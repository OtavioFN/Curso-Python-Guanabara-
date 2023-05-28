'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import date
ano_atual = date.today().year

submit = dict()
submit['nome'] = str(input('Informe seu nome: '))
submit['ano_nasc'] = int(input('Informe seu ano de nascimento: '))
submit['idade'] = ano_atual - submit['ano_nasc']
submit['carteira'] = int(input('Informe o código do seu CTPS (0 para informar que não existe): '))
if submit['carteira'] != 0:
    submit['ano_cont'] = int(input('Informe o ano de contratação: '))
    submit['salario'] = float(input('Informe seu salário:'))
    submit['aposentadoria'] = 65 - submit['idade']
    print(f'Seu nome é {submit["nome"]}')
    print(f'{submit["nome"]} tem {submit["idade"]} anos')
    print(f'O CTPS de {submit["nome"]} tem o valor de {submit["carteira"]}')
    print(f'{submit["nome"]} foi contratado(a) em {submit["ano_cont"]}')
    print(f'{submit["nome"]} vai se aposentar daqui a {submit["aposentadoria"]} anos')
else:
    print(f'Seu nome é {submit["nome"]}')
    print(f'{submit["nome"]} tem {submit["idade"]} anos')
    print(f'{submit["nome"]} não possui carteira de trabalho') 

