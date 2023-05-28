'''Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros'''

preço = float(input('Informe o preço do produto: '))
forma = str(input('''Informe a forma de pagamento: 
(D) Para pagar com dinheiro/cheque!
(C) Para pagar com cartão
''')).upper()
if forma == 'D':
    print(f'O valor a ser pago é de R${preço - (10/100 * preço):.2f}')
elif forma == 'C':
    parcela = int(input('Informe quantas vezes deseja parcelar: '))
    if parcela == 1:
        preço -= 5/100 *preço
        print(f'Você decidiu pagar à vista no cartão, o produto ficará por {preço:.2f}')
    elif parcela <= 2:
        print(f'O preço do produto será de R${preço:.2f}')
    else:
        preço += 20/100 * preço
        print(f'O preço do produto será de R${preço:.2f}, sendo {parcela} parcelas de {preço/parcela:.2f}')
else:
    print('Opção inválida de pagamento! Tente novamente!')
