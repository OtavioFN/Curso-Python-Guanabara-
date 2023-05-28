'''
Funções (parte 2)
* Interactive help
* Docstrings
* Argumentos opcionais
* Escopo de variáveis
* Retorno de resultados
'''

# Interactive help

help(print)

print(input.__doc__)

# Docstring

def contador(i,f,p):
    '''-> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno'''
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim')

contador(0,100,10)

help(contador)

# Parâmetros opcionais

def somar(a,b,c):
    soma = a + b + c
    print(soma)

somar(3,2,5)
# somar(8,4) -> Erro por falta de parâmetros

def somar1(a=0,b=0,c=0): # Parâmetros opcionais
    soma = a + b + c
    print(soma)

somar1(3,2,5)
somar1(8,4)
somar1(b=4,c=2)
somar1(c=1,a=2)

# Escopo de variáveis (local onde a variável VAI ou Não existir)

def teste():
    x = 8 # A variável (x) tem um escopo local (dentro da função)
    print(f'Na função teste, n vale {n}')

#Programa principal
n = 2 # A variável (n) tem um escopo global 
print(f'No programa principal, o n vale {n}')
teste()
# print(f'No programa principal, o x vale {x}') -> retornará um erro pois (x) tem um escopo local

def teste(b):
    global a # Isso faz com que o (a) com escopo local seja utilizado como se tivesse escopo global
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5 # Esse (a) é desconsiderado, sendo utilizado somente o (a) que antes era considerado escopo local
teste(a)
print(f'A fora vale {a}')

# Retorno de resultados

def somar(a=0,b=0,c=0):
    s = a + b + c
    return s


resp = somar(3,2,5)
print(resp)

print(somar(1,2,5))