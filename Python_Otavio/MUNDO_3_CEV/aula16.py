'''Variávies compostas (tuplas)'''
# Existem as tuplas, listas e dicionários
# Tupla é a variáveis que guarda um ou mais de um espaço dentro dela
# lanche = 'hambúrguer' - variável simples
lanche = ('hambúrguer', 'suco', 'pizza', 'pudim') # - variável composta
print(lanche) # imprime todos os lanches

print(lanche[2]) # vai imprimir a pizza, que está no índice 2 (terceira posição)

print(lanche[0:2]) # vai imprimir os lanches do indíce 0 até o índice 1, desconsiderando o 2

print(lanche[1:]) # começa no índice 1 até o índice final

print(lanche[-1]) # imprime o último elemento

print(len(lanche)) # imprime qual o tamanho da variável composta (quantas posições ele ocupa)

print(lanche[-2:]) # vai imprimir começando do -2 até o final da tupla

print(sorted(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}')

print('')

for i in range(0, len(lanche)): # percorrerá a quantidade de elementos da tupla
    print(f'Eu vou comer {lanche[i]} na posição {i}')

print('')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')


'''# As tuplas são imutáveis
# EX:

print(lanche[1])
lanche[1] = 'Refrigerante' # Dará erro pois objetos não podem ser atribuídos em tuplas'''

a = (2,5,4)
b = (5,8,1,2)
c = b + a

print(c) # soma as duas tuplas

print(len(c))

print(c.count(5)) # Informa quantas vezes o número 5 aparece na tupla

print(c.index(8)) # Informa qual a posição do número 8

print(c.index(5)) # Se houver mais de um elemento com a mesma informação, ele retornará a primeira posição na qual foi econtrada o elemento

print(c.index(5,1)) # Nessa situação, utilizamos o 1 dps da vírgula para dizer que queremos saber qual a posição do número 5 após o índice 1 (segunda posição) - Isso é chamado de deslocamento

pessoa = ('Gustavo', 39, 'M', 99.88)  # Podemos utilizar elementos de diferentes tipos em uma tupla
print(pessoa) 
del(pessoa) # A tupla é imutável, porém a única coisa que podemos modificar na tupla é deletar ela por completo
print(pessoa)
