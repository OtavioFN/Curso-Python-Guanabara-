'''Listas (Parte 2)'''

'''dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])
pessoas = list()
pessoas.append(dados[:]) # Copia a lista dados em pessoas, se não tivesse o ":", a lista seria como 1 só, se uma modificar, a outra modifica
print(pessoas[0][0])
pessoas = [['Pedro', 25],['Maria', 19],['João', 32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])'''

'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) 
print(galera)'''

'''galera = [['João', 19],['Ana', 33],['Joaquim', 13],['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[0][0][0])
for pessoa in galera:
    print(pessoa[0]) # vai imprimir somente os nomes'''

galera = list()
dado = list()
idade = 0
for c in range(0,5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    if dado[1] > 21:
        galera.append(dado[:])
    dado.clear()
print(galera)

