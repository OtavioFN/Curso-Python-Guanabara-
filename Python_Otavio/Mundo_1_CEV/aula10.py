'''tempo = int(input('Digite quantos anos tem seu carro?: '))
if tempo <= 3:
  print('Seu carro é novo')
else:
  print('Seu carro é velho!')
print('--FIM--')'''

# if = se
# else = senão
# O comando pra condição if é chamado de bloco verdadeiro
# Ex: print('Seu carro é novo')
# O comando pra condição else é chamado de bloco falso
# Ex: print('Seu carro é velho!')

# OUTRO MODO

'''tempo = int(input('Digite quantos anos tem seu carro?:'))
print('Carro novo'if tempo <= 3 else 'Carro velho')
print('--FIM--')'''

'''nome = str(input('Qual é o seu nome?: ')).strip()
if nome == 'Otávio':
    print('Seu nome é lindo!')
else:
    print('Seu nome é tão normal!')
print(f'Olá, {nome}! Bom dia')'''

'''nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2)/ 2
if media < 6:
    print('Sua média foi ruim! ESTUDE MAIS!')
else: 
    print('Sua média foi boa! PARABÉNS!')
print(f'Sua média foi {media}')'''

# OU

'''nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2)/ 2
print('PARABÉNS!' if media >= 6 else 'ESTUDE MAIS!')'''

nota = float(input('Digite sua nota: '))
if nota >= 6 and nota < 8:
  print('Parabéns')
elif nota >= 8:
  print('Nota excelente!')
else: 
  print('Estude mais!')
print(13%5)
a = 10
a = a /2
print(type(a))
