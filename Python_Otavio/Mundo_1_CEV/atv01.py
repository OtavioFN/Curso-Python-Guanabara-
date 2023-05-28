# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largparede = float(input('Informe a largura da parede em metros: '))
altuparede = float(input('Informe a altura da parede em metros: '))
area = largparede * altuparede
ltinta = area/2
print(f'A dimensão da parede é de {largparede}x{altuparede} e sua área é de {area}m².\nPara pintar essa parede você precisará de {ltinta} litros de tinta.')