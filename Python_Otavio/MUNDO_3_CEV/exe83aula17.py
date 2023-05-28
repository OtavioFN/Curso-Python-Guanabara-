'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
'''expression = str(input('Type ur expression: '))
expression_spl = []
for lt in expression:
    expression_spl.append(lt)

print(expression_spl.count('('))
print(expression_spl.count(')'))
if expression_spl.count('(') == expression_spl.count(')'):
    print('A expressão está correta!')
else:
    print('A expressão está incorreta')'''

expression = str(input('Digite sua expressão: '))
cont = 0

for i in expression:
        if i == '(':
            cont += 1
        elif i ==')':
            cont -= 1
            if cont < 0:
                print('CABOU')
                exit(0)
            if cont != 0:
                print('Cabou')
            else:
                print('Expressão válida')

            #REVER