# Saber o valor do produto com 5% de desconto:

# valorprod = float(input('Informe o valor do produto: R$'))
# prod5pc = valorprod - (valorprod*5/100)
# print(f'O valor do produto é R${valorprod:.2f}, com 5% de desconto o produto custará R${prod5pc:.2f}.')
#-----------

# Saber o salário com 15% de aumento:
# salário = float(input('Informe seu salário: R$'))
# salario15pc = salário + (salário*15/100)
# print(f'Seu salário é de R${salário}, com 15% de aumento seu salário será de R${salario15pc:.2f}.')
#--------

# Valor de um produto com 10% de desconto e 8% a mais (parcelado):
# valorprod = float(input('Informe o valor do produto: R$'))
# produtoàvista = valorprod - (valorprod*10/100)
# produtoparcelado = valorprod + (valorprod*8/100)
# print(f'O valor do produto é R${valorprod}, se você comprá-lo à vista você terá 10% de desconto, assim o produto fica por R${produtoàvista}, mas se você parcelar o valor do produto você terá que pagar 10% a mais pelo mesmo, assim valendo R${produtoparcelado}.')
#---------

# Converter graus celsius em fahrenheit
# gc = float(input('Informe a temperatura em °C:'))
# gf = gc*1.8+32
# print(f'Se a temperatura está em {gc}°C, então está {gf}°F.')
#---------

#  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Por quantos dias você alugou o carro?: '))
km = float(input('Quantos quilômetros foram rodados?: '))
rsdias = dias * 60
rskm = km * 0.15
print(f'Se você alugou o veículo por {dias} dias e rodou {km}km com ele, você pagará R${rsdias + rskm:.2f}.')
print(f'Você pagou R${rsdias:.2f} pelos dias alugados e R${rskm:.2f} por quilômetros rodados.')