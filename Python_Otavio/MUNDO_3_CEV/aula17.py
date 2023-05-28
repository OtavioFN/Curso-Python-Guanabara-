# Variável composta (lista)

snacks = ['Hamburguer', 'juice', 'pizza', 'pudim']
print(snacks[2]) # retornará pizza

# Listas são mutáveis

snacks[3] = 'icecream'
print(snacks)

snacks.append('cookie') # adiciona um elemento à lista
print(snacks)

snacks.insert(0,'hotdog') # adiciona um elemento na posição que eu quero
print(snacks)

# Formas de remover um elemento da lista

# del snacks[3]
# snacks.pop(3) # o snack.pop() - sem parâmetro, ele eliminará o último elemento da lista
snacks.remove('pizza')
print(snacks)

# Se tentarmos eliminar um elemento que não existe na lista retornará um erro do python. Portanto podemos eliminar usando a condicional if
# Ex:
'''if 'pizza' in snacks:
        snacks.remove('pizza')''' 

# Se chamarmos um método para eliminar um elemento da string e possuem dois elementos igual na mesma, o método eliminará o primeiro elemento que possua o valor que eu queira eliminar
# EX:
num = [7,2,5,3,2,1]
num.remove(2)
print(num)

values = list(range(4,11)) # criar uma lista com range
print(values)

numbers = [8,2,5,4,9,3,0]
numbers.sort() # ordena a lista
print(numbers)

numbers.sort(reverse=True) # ordena a lista de forma reversa
print(numbers)

print(len(numbers)) # retorna quantos espaços a lista ocupa 

# Quando igualamos uma lista à outra, as listas SEMPRE terão os mesmos valores
# EX: 
a = [2,3,4,7]
b = a
print(a)
print(b)
b.append(7)
print(a)
print(b)

# Para resolvermos esse problema, devemos fazer o seguinte:

c = [1,2,3,4]
d = c[:]
print(c)
print(d)
d.append(5)
print(c)
print(d)

