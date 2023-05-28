# SISTEMA DE ÔNIBUS
# VERIFICA SE A CAPACIDADE FOI ATINGIDA

capacidade = 0
while capacidade <= 11:
    problema = int(input('Problema?\nSim [1]\nNão [2]'))
    print(f'Vagas diponíveis {10-capacidade}')
    entra = input('Vai entrar?:\nSim [s]\nNão [n]').lower()

    if problema == 1:
        break

    if entra == 's': #if entra == 's' or entra == 'S'
        capacidade += 1
print(f'O ônibus está com {capacidade} passageiros')