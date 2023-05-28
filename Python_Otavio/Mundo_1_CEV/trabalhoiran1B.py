'''Crie um gerador de dados aleatórios para um usuário fictício, contendo:

▸ Nome completo (um nome e um sobrenome apenas, ex.: João Silva)

▸ O nome deve ser escolhido aleatoriamente de uma lista com pelo menos 10 nomes

▸ O sobrenome deve ser escolhido aleatoriamente de uma lista diferente, contendo ao
menos 10 sobrenomes

▸ CPF, no formato XXX.XXX.XXX-XX (onde X é um número aleatório de 0 a 9). Não é preciso
que o número gerado seja válido (ou seja, que tenha os dígitos verificadores corretos).

▸ E-mail. O e-mail deve obrigatoriamente estar no formato nome.sobrenome@domínio, onde o
nome e o sobrenome devem corresponder aos valores já sorteados para compor o nome
completo (mas em minúsculas) e o domínio deve ser escolhido aleatoriamente de uma lista
com pelo menos 5 domínios.'''

'''▸ Nome: Bruna Dantas

▸ CPF: 061.274.295-39

▸ E-mail:

bruna.dantas@gmail.com'''

import random as r
x1 = str(r.randint(1,9))
x2 =str(r.randint(1,9))
x3 = str(r.randint(1,9))
x4 = str(r.randint(1,9))
x5 = str(r.randint(1,9))
x6 = str(r.randint(1,9))
x7 = str(r.randint(1,9))
x8 = str(r.randint(1,9))
x9 = str(r.randint(1,9))
x10 = str(r.randint(1,9))
x11 = str(r.randint(1,9))
nomes_para_sorteio = ['Otávio', 'Sérgio', 'Loren', 'Ester', 'Kaline', 'Otaviano', 'Renata', 'Maria', 'Julya', 'Beatriz']
sobrenomes_para_sorteio = ['Silva', 'Fernandes', 'Oliveira', 'Lívio', 'Cabral', 'Souza', 'Guedes', 'Vieira', 'Lima', 'Albuquerque']
dominios_para_sorteio = ['@gmail.com','@hotmail.com','@outlook.com','@yahoo.com','@aluno.ifal.edu.br']
cpf_gerado = x1+x2+x3+'.'+x4+x5+x6+'.'+x7+x8+x9+'.'+x10+x11
nome = r.choice(nomes_para_sorteio)
sobrenome = r.choice(sobrenomes_para_sorteio)
gmail = r.choice(dominios_para_sorteio)
print(f'''Nome: {nome} {sobrenome}
CPF: {cpf_gerado}
E-mail: {nome.lower()}.{sobrenome.lower()}{gmail}''')
