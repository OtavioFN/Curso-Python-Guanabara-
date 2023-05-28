# import math
# ceil - arredonda pra cima
# floor - arredonda p baixo
# trunc - elimina da vírgula p frente
# pow - potência
# sqrt - raíz quadrada
# factorial - fatorar

# import math : importa tudo
# from math import sqrt : importa só o sqrt (no caso)
# from math import sqrt,ceil : importa as duas (no caso)

# import math
# num = int(input('Digite um número: '))
# raíz = math.sqrt(num)
# print(f'A raíz de {num} é igual a {raíz:.2f}')

# from math import sqrt, ceil
# num = int(input('Digite um número: '))
# raíz = sqrt(num)
# print(f'A raíz de {num} é igual a {ceil(raíz):.2f}')

# import random
# num = random.randint(1, 10)
# print(num)

# from math import sqrt as raíz
# print(f'Raíz de 9 é {raíz(9)}')

# Área de um círculo: π * Raio²
# Circunferência de um círculo: 2 * π * Raio
'''from math import sqrt as raíz, pi, pow
raio = float(input('Informe o raio do círculo: '))
circunferencia = 2 * pi * raio
print(f'A cincurferência do círculo é: {circunferencia}')
area = pi * pow(raio, 2)
print(f'A área do círculo é: {area}')'''

#import random
#random.random(): Sorteia um número float entre 0 e 1

'''import random
print(random.random())'''

#random.randrange(x, y) : sorteia entre dois números escolhidos, com exceção do último número (no caso o y)
#OBS random.randrange(x, y, z) : sorteia entre dois números escolhidos, com exceção do último (no caso o y) com espaçamento entre (z) números

'''import random
print(random.randrange(1, 6))
print(random.randrange(2, 6, 2))'''

# Ex: print(random.randrange(2, 6, 2)) - Sorteio entre 2 e 6, com exceção do 6, com espaço de 2 em dois números = 2,4 nesse caso

# random.randint(x, y): Sorteia um número entre x e y (INCLUINDO O Y)

#----------

alunos = ['Claudin', 'Dagoberto', 'Jorgin']
print(alunos)
# Como sortear um valor da lista:
import random
print(random.choice(alunos))
# Como embaralhar os valores da lista
random.shuffle(alunos)
print(alunos)

