'''O verão está chegando e, com ele, o calor. Nessa época do
ano é natural que o uso mais frequente doar-condicionado
resulte em contas mais altas no fim do mês.

▸ Assim, construa um programa que calcule o gasto em reais decorrente do

uso do ar-condicionado

▸ O programa deverá perguntar ao usuário quantas horas em média o ar-
condicionado é utilizado por dia, quantos dias em média é utilizado por mês,

o consumo do aparelho em kW/h e o valor do kWh cobrado pela companhia
elétrica, informando, em resposta, o valor resultante na conta de energia'''

'''Para o cálculo, basta

usar a fórmula a seguir:

▸ Ex.: um ar-condicionado
ligado 8 horas por dia,
por 20 dias, que
consome 17,1 kW/h
com uma tarifa de
R$ 1,136987 resulta em um gasto mensal de R$ 103,69

▸ O valor resultante deve ser exibido com 2 casas decimais

INTRODUÇÃO À PROGRAMAÇÃO

EXERCÍCIO AVALIATIVO 1A

3

FÓRMULA PARA CALCULAR O GASTO DECORRENTE
DO CONSUMO DE ENERGIA DO AR-CONDICIONADO

MÉDIA DE
HORAS
X
MÉDIA DE
DIAS
X
CONSUMO
kW/h
X
TARIFA DE
ENERGIA
/
30 DIAS'''

hr = float(input('Informe quantas horas em média o ar-condicionado é utilizado por dia: '))
dias = int(input('Informe quantos dias o ar-condicionado é utilizado por mês: '))
valor_kw_ar = float(input('Informe o consumo do aparelho em Kw/h: '))
valor_kw_companhia = float(input('Informe quantos Kw/h a companhia cobra: '))
valor_conta_energia = (hr*dias*valor_kw_ar*valor_kw_companhia)/30
print(f'Um ar-condicionadoligado {hr} horas por dia, por {dias} dias, que consome {valor_kw_ar} kW/h com uma tarifa de R$ {valor_kw_companhia} resulta em um gasto mensal de R$ {valor_conta_energia:.2f}')
