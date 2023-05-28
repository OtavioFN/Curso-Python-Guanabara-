'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

Number_List = []
while True:
    n = int(input('Type a value: '))
    if n in Number_List:
        print('This value already is in the list...')
    else:
        Number_List.append(n)
        print('Number added sucessfully!')
    proceed = str(input('Do you want to continue? [Y/N]: ')).strip().upper()
    while proceed not in 'YN':
        proceed = str(input('Do you want to continue? [Y/N]: ')).strip().upper()
    if proceed == 'N':
        break
Number_List.sort()
print(f'The ordened list is {Number_List}')