'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. 
Para os inferiores ou iguais, o aumento é de 15%.'''
salario = float(input('Informe o seu salário R$: '))
if salario <= 1250:
    salario_aumento = (15/100*salario)+salario
    print(f'Seu salário atual é de R$ {salario:.2f}, com o aumento, o salário será de R$ {salario_aumento:.2f} !')
else:
    salario_aumento = (10/100*salario)+salario
    print(f'Seu salário atual é de R$ {salario:.2f}, com o aumento, o salário será de R$ {salario_aumento:.2f} !')
