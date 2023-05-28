# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira:

"""from math import trunc
num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {trunc(num)}')"""

# ------------ OU

'''from math import floor
num = float(input('Informe um número: '))
print(f'O número {num} tem a parte inteira {floor(num)}')'''

# ------------- OU

'''from math import ceil
num = float(input('Informe um número: '))
print(f'O número {num} tem a parte inteira {ceil(num-1)}')'''

# ------------- OU

'''num = float(input('Digite um valor: '))
print(f'O número {num} tem a porção inteira {int(num)}')'''

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

'''from math import pow, sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = pow(co, 2) + pow(ca, 2)
print(f'A hipotenusa do triângulo vai medir {sqrt(hi):.2f}')'''

#-------------- OU:

'''co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A medida da hipotenusa é {hi:.2f}')'''

#-------------- OU:

'''from math import hypot
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {hypot(co, ca):.2f}')
# OU
# hi = hypot(co, ca)
#print(f'A hipotenusa vai medir {hi:.2f}')'''

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.:

'''from math import radians, cos, sin, tan
ângulo = int(input('Digite o ângulo que você deseja: '))
an = radians(ângulo)
cos = cos(an)
sen = sin(an)
tan = tan(an)
print(f'O ângulo é de {ângulo} graus.')
O valor do seu seno é {sen:.2f}.')
print(f'O valor do seu cosseno é {cos:.2f}.')
print(f'O valor da sua tangente é {tan:.2f}.')'''

#--------------OU: Fica mais feio bruh

'''from math import radians, cos, sin, tan
ângulo = int(input('Digite o ângulo que você deseja: '))
cos = cos(radians(ângulo))
sen = sin(radians(ângulo))
tan = tan(radians(ângulo))
print(f'O ângulo é de {ângulo} graus.')
print(f'O valor do seu seno é {sen:.2f}')
print(f'O valor do seu cosseno é {cos:.2f}')
print(f'O valor da sua tangente é {tan:.2f}')'''

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

'''import random
a1 = input('Informe o nome do primeiro aluno(a): ')
a2 = input('Informe o nome do segundo aluno(a): ')
a3 = input('Informe o nome do terceiro aluno(a): ')
a4 = input('Informe o nome do terceiro aluno(a): ')
alunos = [a1, a2, a3, a4]
escolha = random.choice(alunos)
print(f'O escolhido foi {escolha}.')'''

# Gerando um múltiplo de 5 entre 1 e 100:

'''import random
print(random.randrange(5, 101, 5))'''

# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.:

'''import random
a1 = input('Digite o nome do aluno(a): ')
a2 = input('Digite o nome do aluno(a): ')
a3 = input('Digite o nome do aluno(a): ')
a4 = input('Digite o nome do aluno(a): ')
aluno = [a1, a2, a3, a4]
random.shuffle(aluno)
print(f' A ordem será {aluno}')
print(aluno)'''

#OBS: A lista fica embaralhada após o comando, não temporariamente:

#''''''''''''''''

#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

'''import pygame
pygame.init()
pygame.mixer.music.load('Ret.Python.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''
