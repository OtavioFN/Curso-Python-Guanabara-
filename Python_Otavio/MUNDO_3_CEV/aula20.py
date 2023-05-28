'''Função'''


def lin():
    print('-' * 30)

lin()
print('Curso em vídeo')
lin()
lin()
print('Aprenda Python')
lin()
lin()
print('Gustavo Guanabara')
lin()

def frase(nome):
    lin()
    print(nome)
    lin()

frase('Otávio Fernandes')

a = 4 
b = 5 
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2 
b = 1
s = a + b
print(s)

def soma(a,b):
    soma = a + b
    print(soma)


soma(4,5)
soma(8,9)
soma(2,1)

def contador(*num):
    for valor in num:
        print(valor,end=' ')
    print()
    print(len(num))


contador(2,1,7)


def dobra(lista):
    new_list = list()
    for num in lista:
        new_list.append(num*2)
    print(new_list)


def dobra2(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)

valores = [7,2,5,0,4]
dobra(valores)
dobra2(valores)


def soma2(* valores):
    soma = 0
    for valor in valores:
        soma += valor
    print(soma)

soma2(1,2,3,4,4,5)