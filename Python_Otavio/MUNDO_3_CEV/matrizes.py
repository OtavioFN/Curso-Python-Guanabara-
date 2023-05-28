'''m = [[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]
odd = []
soma = 0
mul = 1
maior3col = 0
diagonal_principal = []

for i in range(0, 4):
    for j in range(0, 4):
        m[i][j] = int(input(f"Informe um número para linha {i} e coluna {j} : "))
        if i == j:
            soma += m[i][j]
        if i == 1:
            mul *= m[i][j]
        if j == 1 or j == 1 and m[i][j] > maior3col:
            maior3col = m[i][j]

for k in range(4):
    for l in range(4):
        print(m[k][l], end=' ')
    print()

print(soma)
print(mul)
print(maior3col)'''

'''m = [[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]
diagonal_principal = []
triangulo_inferior = []
triangulo_superior = []

for i in range(0, 4):
    for j in range(0, 4):
        m[i][j] = int(input(f"Informe um número para linha {i} e coluna {j} : "))
        if i == j:
            diagonal_principal.append(m[i][j])
        elif i == 0 and j in (1,2,3) or i == 1 and j in (2,3) or i == 2 and j == 3:
            triangulo_superior.append(m[i][j])
        else:
            triangulo_inferior.append(m[i][j])

for k in range(4):
    for l in range(4):
        print(m[k][l], end=' ')
    print()

opcao = 0

while True:
    print("""[1] - Exibir Diagonal Principal
[2] - Exibir Triângulo Superior
[3] - Exibir Triângulo Inferior
[4] - Sair""")
    opcao = int(input("Informe um número: "))
    if opcao == 1:
        for i in range(4):
            for j in range(4):
                if m[i][j] in diagonal_principal:
                    print(m[i][j], end =' ')
                else:
                    print(' ',end = ' ')
            print()
    elif opcao == 2:
        for i in range(4):
            for j in range(4):
                if m[i][j] in triangulo_superior:
                    print(m[i][j], end =' ')
                else:
                    print(' ',end = ' ')
            print()
    elif opcao == 3:
        for i in range(4):
            for j in range(4):
                if m[i][j] in triangulo_inferior:
                    print(m[i][j], end =' ')
                else:
                    print(' ',end = ' ')
            print()
    elif opcao == 4:
        break'''

jogo_da_velha = [[0],[1], [2]], [[3],[4], [5]], [[6],[7], [8]]

while True:
    for k in range(0,3):
        for l in range(0,3):
            print(f'| {jogo_da_velha[k][l][0]} |', end=' ')
        print()
    posicao = int(input("Deseja Marcar em qual posição (X): "))
    for p in range(0,3):
        for q in range(0,3):
            if jogo_da_velha[p][q][0] == posicao:
                jogo_da_velha[p][q] = 'X'
    if jogo_da_velha[0][0] == 'X' and jogo_da_velha[0][1] == 'X' and jogo_da_velha[0][2] == 'X':
        for k in range(0,3):
            for l in range(0,3):
                print(f'| {jogo_da_velha[k][l][0]} |', end=' ')
            print()
        print('O X VENCEU!!')
        break
    elif jogo_da_velha[1][0] == 'X' and jogo_da_velha[1][1] == 'X' and jogo_da_velha[1][2] == 'X':
        for k in range(0,3):
            for l in range(0,3):
                print(f'| {jogo_da_velha[k][l][0]} |', end=' ')
            print()
        print('O X VENCEU!!')
        break
    elif jogo_da_velha[2][0] == 'X' and jogo_da_velha[2][1] == 'X' and jogo_da_velha[2][2] == 'X':
        for k in range(0,3):
            for l in range(0,3):
                print(f'| {jogo_da_velha[k][l][0]} |', end=' ')
            print()
        print('O X VENCEU!!')
        break
    elif jogo_da_velha[0][0] == 'X' and jogo_da_velha[1][0] == 'X' and jogo_da_velha[2][0] == 'X':
        for k in range(0,3):
            for l in range(0,3):
                print(f'| {jogo_da_velha[k][l][0]} |', end=' ')
            print()
        print('O X VENCEU!!')
        break
    elif jogo_da_velha[0][1] == 'X' and jogo_da_velha[1][1] == 'X' and jogo_da_velha[2][1] == 'X':
        for k in range(0,3):
            for l in range(0,3):
                print(f'| {jogo_da_velha[k][l][0]} |', end=' ')
            print()
        print('O X VENCEU!!')
        break
    elif jogo_da_velha[0][2] == 'X' and jogo_da_velha[1][2] == 'X' and jogo_da_velha[2][2] == 'X':
        for k in range(0,3):
            for l in range(0,3):
                print(f'| {jogo_da_velha[k][l][0]} |', end=' ')
            print()
        print('O X VENCEU!!')
        break
    elif jogo_da_velha[0][0] == 'X' and jogo_da_velha[1][1] == 'X' and jogo_da_velha[2][2] == 'X':
        for k in range(0,3):
            for l in range(0,3):
                print(f'| {jogo_da_velha[k][l][0]} |', end=' ')
            print()
        print('O X VENCEU!!')
        break
    elif jogo_da_velha[0][2] == 'X' and jogo_da_velha[1][1] == 'X' and jogo_da_velha[2][2] == 'X':
        for k in range(0,3):
            for l in range(0,3):
                print(f'| {jogo_da_velha[k][l][0]} |', end=' ')
            print()
        print('O X VENCEU!!')
        break
    for k in range(0,3):
        for l in range(0,3):
            print(f'| {jogo_da_velha[k][l][0]} |', end=' ')
        print()
    posicao = int(input("Deseja Marcar em qual posição (O): "))
    for p in range(0,3):
        for q in range(0,3):
            if jogo_da_velha[p][q][0] == posicao:
                jogo_da_velha[p][q] = 'O'
    if jogo_da_velha[0][0] == 'O' and jogo_da_velha[0][1] == 'O' and jogo_da_velha[0][2] == 'O':
        for k in range(0,3):
            for l in range(0,3):
                print(f'| {jogo_da_velha[k][l][0]} |', end=' ')
            print()
        print('O (O) VENCEU!!')
        break
    elif jogo_da_velha[1][0] == 'O' and jogo_da_velha[1][1] == 'O' and jogo_da_velha[1][2] == 'O':
        for k in range(0,3):
            for l in range(0,3):
                print(f'| {jogo_da_velha[k][l][0]} |', end=' ')
            print()
        print('O (O) VENCEU!!')
        break
    elif jogo_da_velha[2][0] == 'O' and jogo_da_velha[2][1] == 'O' and jogo_da_velha[2][2] == 'O':
        for k in range(0,3):
            for l in range(0,3):
                print(f'| {jogo_da_velha[k][l][0]} |', end=' ')
            print()
        print('O (O) VENCEU!!')
        break
    elif jogo_da_velha[0][0] == 'O' and jogo_da_velha[1][0] == 'O' and jogo_da_velha[2][0] == 'O':
        for k in range(0,3):
            for l in range(0,3):
                print(f'| {jogo_da_velha[k][l][0]} |', end=' ')
            print()
        print('O (O) VENCEU!!')
        break
    elif jogo_da_velha[0][1] == 'O' and jogo_da_velha[1][1] == 'O' and jogo_da_velha[2][1] == 'O':
        for k in range(0,3):
            for l in range(0,3):
                print(f'| {jogo_da_velha[k][l][0]} |', end=' ')
            print()
        print('O (O) VENCEU!!')
        break
    elif jogo_da_velha[0][2] == 'O' and jogo_da_velha[1][2] == 'O' and jogo_da_velha[2][2] == 'O':
        for k in range(0,3):
            for l in range(0,3):
                print(f'| {jogo_da_velha[k][l][0]} |', end=' ')
            print()
        print('O (O) VENCEU!!')
        break
    elif jogo_da_velha[0][0] == 'O' and jogo_da_velha[1][1] == 'O' and jogo_da_velha[2][2] == 'O':
        for k in range(0,3):
            for l in range(0,3):
                print(f'| {jogo_da_velha[k][l][0]} |', end=' ')
            print()
        print('O (O) VENCEU!!')
        break
    elif jogo_da_velha[0][2] == 'O' and jogo_da_velha[1][1] == 'O' and jogo_da_velha[2][2] == 'O':
        for k in range(0,3):
            for l in range(0,3):
                print(f'| {jogo_da_velha[k][l][0]} |', end=' ')
            print()
        print('O (O) VENCEU!!')
        break



