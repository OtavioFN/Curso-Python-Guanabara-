''' Aprimore o desafio anterior, mostrando no final:                                                    
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

odd_sum = 0
third_column_sum = 0
biggest_second_column_number = 0

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l, c}]: '))
        if matriz[l][c] % 2 == 0:
            odd_sum += matriz[l][c]
        if c == 2:
            third_column_sum += matriz[l][c]
        if l == 1 and c == 0 or l == 1 and matriz[l][c] > biggest_second_column_number:
            biggest_second_column_number = matriz[l][c]

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma de todos os valores pares digitados é {odd_sum}')
print(f'A soma dos valores da terceira coluna é de {third_column_sum}')
print(f'O maior valor da segunda linha é {biggest_second_column_number}')


