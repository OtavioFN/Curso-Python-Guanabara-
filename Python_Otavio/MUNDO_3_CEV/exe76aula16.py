'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

products = ('Pencil', 1.75, 'Eraser', 2.00, 'Notebook', 15.90, 'Pencil case', 25.00, 'protractor', 4.20, 'Compass', 9.99, 'Bag', 120.32, 'Pens', 22.30, 'Book', 34.90)
print('-'*40)
print(f"{'PRICES TABLE':^40}")
print('-'*40)
for pos in range(0,len(products)):
    if pos % 2 == 0:
        print(f'{products[pos]:.<30}', end ='') # Escreve a String com a quantidade de 30 caracteres e preenche os caracteres vazios com o ponto ('.') que eu coloquei
    else:
        print(f'${products[pos]:>7.2f}') # Preço alinhado a direita com 7 caracteres e com duas casas flutuantes



# print(f'{"Otávio":30}!') - Escreve a String com a quantidade de caracteres que eu quis (30)
