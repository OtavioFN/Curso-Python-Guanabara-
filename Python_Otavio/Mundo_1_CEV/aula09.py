#Manipulação de cadeias de textos
# OBS: Uma string é imutável
frase = 'Curso em Vídeo Python'
print(frase [9])
# Mostra o caractere no índice 9
print(frase[9:13])
# Vai retornar do índice 9 até o 13 (incluido o 9 e excluindo o 13)
print(frase[9:21])
# Retorna assim do índice 9 até o fim da frase, já que a mesma tem 20 índices
print(frase[9:21:2])
# Vai retornar do índice 9 até o 20, pulando de 2 em 2 caracteres
print(frase[:5])
# Vai do índice 0 até o índice digitado (excluindo o 5° índice)
print(frase[15:])
# Retorna do índice 15 até o caractere final
print(frase[9::3])
# Retorna a frase do índice 9, até o final, pulando de 3 em 3 caracteres
#------------------------------
#Análise:
print(len(frase))
# Retorna o tamanho da frase, quantos caracteres ela possui
print(frase.count('o'))
# Retorna quantas vezes aparece a 'o' (minúscula no caso)
print(frase.count('o',0,13))
# Retorna quantas vezes o 'o' aparece entre o índice 0 ao 13 (ignorando o 13)
print(frase.find('deo')) 
# Retorna em qual posição o 'deo' começa
print(frase.find('Android'))
# Informa (-1) pois não foi encontrado
print('Curso' in frase)
# Retorna se 'Curso' se encontra em frase, dizendo True ou False
#----------------------
# Transformação
print(frase.replace('Python','Android'))
# Substitue algo na str por outro
print(frase.upper())
# Retorna a frase com todos os caracteres maiúsculos
print(frase.lower())
# Retorna a frase mantendo as minúsculas e tranformando as maiúsculas em minúsculas
print(frase.capitalize())
# Tranforma o primeiro caractere em maiúsculo e tranforma todo o resto em minúsculo
print(frase.title())
# Tranforma todas as primeiras letras de todas as palavras em maiúsculo
frase_teste = '   Aprenda Python  '
print(frase_teste)
print(frase_teste.strip())
# Remove todos os espaços desnecessários na frase
print(frase_teste.rstrip())
# Remove somente os espaços desnecessários do lado direito da frase
print(frase_teste.lstrip())
# Remove somente os espaços desnecessários do lado esquerdo da frase
#--------------------------
# Divisão
print(frase.split()) #OBS: ESTUDAR SPLIT
# Divide a frase de acordo com os espaços
# -------------------
# Junção
print('-'.join(frase))
# Junta os conjuntos de caracteres anteriormente divididos
print('''Acharam que eu estava derrotado
Quem achou estava errado
Eu voltei, tô aqui
Se liga só, escuta aí
Ao contrário do que você queria
Tô firmão, tô na correria
Sou guerreiro e não pago pra vacilar
Sou vaso ruim de quebrar
Oitavo anjo do Apocalipse
Tenebroso como um eclipse''')
# Colocar três aspas (duplas ou não) no começo ou no fim de um print muito longo, faz com que ele retorne normalmente o que eteja escrito
print(frase.count('O'))
# Retorna a quantidade de vezes que o 'O' aparece (tem que ser exatamente maiúsculo)
print(frase.upper().count('O'))
# Aqui ele tranformou toda a frase em maiúscula e pediu para retornar quantos 'O's tem na frase, ou seja, ele retornará o total de 'o's na frase, sejam maiúsculos ou minúsculos
frase_teste2 = '   Curso em Vídeo Python   '
print(len(frase_teste2))
# Retornará o tanto de caracteres que possui a frase_teste2 (o espaço também é considerado um caractere)
print(len(frase_teste2.strip()))
# Como o strip remove todos os espaços desnecessários da frase, se eu pedir o len dessa frase ele retornará o tamanho da frase sem nenhum caractere(espaço) desnecessário
print(frase.replace('Python', 'Android'))
# Trocará a palavra Python por Android
print(len(frase.replace('Python', 'Android')))
# Retornará o tamanho da frase com a palavra Android no lugar de Python
print('Curso' in frase)
# Retornará, em forma de True ou False, se o conjunto de caracteres escrito está contido na frase
print('curso' in frase)
# Aqui retornará False pois o c de curso está em minúsculo, diferente da frase original
print(frase.find('Curso'))
# Dirá em qual índice o conjunto ou caractere se inicia ou onde está contido
print(frase.find('curso'))
# Aqui ele retornará -1 pois 'curso' com c minúsculo não existe na frase
print(frase.rfind('o'))
# Ele retornará a posição onde está contido o caractere ou conjunto de caractere começando do final da string
print(frase.lower().find('curso'))
# Com o .lower() tranformando toda a frase em minúscula, logo será possível encontrar 'curso' com c minúsculo na frase
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
# Mesmo conceito do anterior
print(frase.split())
# Divide a frase de acordo com os espaços
dividido = frase.split()
print(dividido[0])
# Aqui ele retornou o primeiro elemtento da frase splitada, que no caso é a que está no índice 0
print(dividido[2][3])
# Aqui ele pegou o elemento de índice 2 [2] da frase splitada (Vídeo), e retornou o caractere de índice 3 [3] do elemento anteriormente selecionado (e)
#-----------------------
# Separar o nome dos sobrenomes
'''name = 'Cláudio Buchecha Damariz'
splited_name = name.split(' ', 1)
first_name = splited_name[0]
surnames = ' '.join(splited_name[1:])
print(first_name)
print(surnames)'''
