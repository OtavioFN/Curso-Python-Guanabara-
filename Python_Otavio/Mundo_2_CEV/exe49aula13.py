# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
tab = int(input('Digite o número ao qual deseja ver a tabuada: '))
for i in range(1, 11):
    print(f'{tab} x {i} = {tab*i}')