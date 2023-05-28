'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

casa = float(input('Qual o valor da casa: R$ '))
salario = float(input('Informe seu salário: R$ '))
anos = int(input('Em quantos anos você deseja pagar?: '))
meses = anos*12
prestaçao = casa / meses
print(f'Financiar uma casa de R$ {casa} em {anos} anos a prestação mensal ficará por R$ {prestaçao:.2f}')
if prestaçao > 30/100 * salario:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo CONCEDIDO!')