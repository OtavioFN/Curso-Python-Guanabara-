'''Variável Composta (Dicionário)'''

dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])

dados = dict()
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])
print(dados['idade'])

# Append não funciona em dicionários

dados['sexo'] = 'M'
print(dados['sexo'])

del dados['idade'] # elimina o elemento e o valor de idade

filme = {
'titulo':'Star Wars',
'ano':1977,
'diretor':'George Lucas'
}
filme1 = {
'titulo':'Avengers',
'ano':2012,
'diretor':'Joss Whedon'  
}
filme2 = {
'titulo':'Matrix',
'ano':1999,
'diretor':'Wachowski'
}

# Cada elemento é chamado de key

print(filme.values()) # Informa os valores

print(filme.keys()) # Informa os elementos (chaves)

print(filme.items()) # retorna tudo

for k, v in filme.items():
    print(f'O {k} é {v}')

locadora = list()

locadora.append(filme)
locadora.append(filme1)
locadora.append(filme2)

print(locadora[0]['ano'])
print(locadora[2]['titulo'])
print()

pessoas = {'nome': 'Gustavo','sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys()) # mostra as chaves
print(pessoas.values()) # retorna os valores
print(pessoas.items()) # retorna tudo
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']
print(pessoas)

pessoas['nome'] = 'Leandro'
print(pessoas)

pessoas['peso'] = 98.5
print(pessoas)

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

estado = dict()
país = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    país.append(estado.copy())
for e in país:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8,}

conjunto_uniao = conjunto.union(conjunto2) # Conjunto dos dois dicionários
print(f'União: {conjunto_uniao}')

conjunto_interseccao = conjunto.intersection(conjunto2) # Elementos que estão nos dois conjuntos
print(f'Intersecção: {conjunto_interseccao}')

conjunto_diferenca = conjunto.difference(conjunto2) # O que tem de diferente entre os dois conjuntos
conjunto_diferenca2 = conjunto2.difference(conjunto)
print(conjunto_diferenca)
print(conjunto_diferenca2)

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
conjunto_diff_simetrica2 = conjunto2.symmetric_difference(conjunto) # Mesmo retorno
print(conjunto_diff_simetrica)
print(conjunto_diff_simetrica2) # Mesmo retorno

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
conjunto_subset = conjunto_b.issubset(conjunto_a)
conjunto_subset2 = conjunto_a.issubset(conjunto_b)

print(f'Conjunto B é um subconjunto de A?: {conjunto_subset}')
print(f'Conjunto A é um subconjunto de B?: {conjunto_subset2}')

lista = ['cachorro', 'gato', 'elefante']



