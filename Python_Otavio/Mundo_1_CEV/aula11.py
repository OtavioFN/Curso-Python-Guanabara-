# \033[0;33;44m

# style;text;back

# são 4 códigos para style

# 0: nenhum estilo
# 1: coloca o texto em negrito
# 2: semi-transparente
# 3: Itálico
# 4: deixa o texto sublinhado
# 5: Texto piscante
# 6 - Não existe
# 7: inverte a cor do texto com o fundo
# 8: Texto invisível
# 9: Riscado 

'''Tipos de cor para texto:

30: preto
31: vermelho
32: verde
33: amarelo
34: azul
35: magenta
36: ciano
37: branco

Tipos de cor de fundo (back) de background:

40: preto
41: vermelho
42: verde
43: amarelo
44: azul
45: magenta
46: ciano
47: branco

print('\033[0;30;41mTeste') # Letra preta fundo vermelho
print('\033[4;33;44mTeste') # Letra amarela sublinhada e fundo azul
print('\033[1;35;43mTeste') # Letra magenta em negrito e fundo amarelo
print('\033[37;42mTeste') # Letra branca e fundo verde
print('\033[37mTeste') # Letra cinza fundo preto (padrão)
print('\033[7;30mTeste') # Letra preta fundo branco'''

# Estudar módulo colorize

a = 3
b = 5

print(f'Os valores são \033[0;41m{a}\033[m e \033[0;44m{b}\033[m')

cores = {'limpa':'\033[m', 'fundovermelho':'\033[41m','fundomagenta':'\033[44m'}
print(f'Os valores são {cores["fundovermelho"]}{a}{cores["limpa"]} e {cores["fundomagenta"]}{b}{cores["limpa"]}')

print('\033[34;43m' + 'Letra azul, fundo amarelo' + '\033[0m')

print('\033[31m' + 'Teste' + '\033[0m')
class bcolors:
    OK = '\033[32m'
    WARNING = '\033[33m'
    FAIL = '\033[31m'
    CLEAN = '\033[0m'

print(bcolors.OK + 'File saved sucessfully!' + bcolors.CLEAN)
print(bcolors.WARNING + 'Warning! Are you sure you want to continue?')
print(bcolors.FAIL + 'Unable to delete record' + bcolors.CLEAN)

# Pode ser retornado assim, ou:

print(f'{bcolors.OK}File saved sucessfully!{bcolors.CLEAN}')
print(f'{bcolors.WARNING}Warning: Are you sure you want to continue?{bcolors.CLEAN}')
print(f'{bcolors.FAIL}Unable to delete record{bcolors.CLEAN}')

import colorama 
from colorama import Fore
from colorama import Style

# Fore: primeiro plano / Frente (foreground)
# Back: fundo / costas (background)

colorama.init()
print(Fore.BLUE + Style.BRIGHT + 'This is the color of the sky' + Style.RESET_ALL)
print(Fore.GREEN + 'This is the color of the grass' + Style.RESET_ALL)
print(Fore.BLUE + Style.DIM + 'This is a dimmer version of the sky' + Style.RESET_ALL)
print(Fore.YELLOW + 'This is the color of the sun' + Style.RESET_ALL)
 
# Bright: Claro (Tonalidade)
# Dim: Escuro (Tonalidade) - Meio transparente

# EXPANSÃO IRAN

import colorama

# colorama.Fore.GREEN

print(colorama.Fore.GREEN + 'Testando módulo Colorama...')
print('Essa linha de baixo também estará colorida!')

# Temos que fazer:

print(colorama.Fore.GREEN + 'Testando módulo Colorama...' + colorama.Style.RESET_ALL)
print('Essa linha de baixo não estará mais colorida!')

# Para ajudar no uso do Módulo

import colorama as c

# Ou seja:

print(c.Fore.GREEN + c.Back.LIGHTGREEN_EX + 'Testando módulo Colorama...' + c.Style.RESET_ALL)

# Aplicamos o módulo utilizando ele em conjunto com o símbolo "+" ou podemos usálos em f-strings:
#Ex:

print(f'{c.Fore.LIGHTYELLOW_EX}{c.Back.BLACK}Texto amarelo com fundo preto!{c.Style.RESET_ALL}')

# Deste jeito acima. {F-string}

print(c.Fore.LIGHTRED_EX + c.Back.YELLOW + c.Style.DIM + 'Texto apagadinho' + c.Style.RESET_ALL)

print(c.Back.BLACK + '                     ' + c.Style.RESET_ALL)
print(c.Back.RED + '                     ' + c.Style.RESET_ALL)
print(c.Back.BLUE + '                     ' + c.Style.RESET_ALL)
print(c.Back.GREEN + '                     ' + c.Style.RESET_ALL)
print(c.Back.MAGENTA + '                     ' + c.Style.RESET_ALL)
print(c.Back.WHITE + '                     ' + c.Style.RESET_ALL)
print(c.Back.YELLOW + '                     ' + c.Style.RESET_ALL)
print(c.Back.CYAN + '                     ' + c.Style.RESET_ALL)
print(c.Back.LIGHTBLUE_EX + '                     ' + c.Style.RESET_ALL)
print(c.Back.LIGHTCYAN_EX + '                     ' + c.Style.RESET_ALL)
print(c.Back.LIGHTYELLOW_EX + '                     ' + c.Style.RESET_ALL)
print(c.Back.LIGHTWHITE_EX + '                     ' + c.Style.RESET_ALL)
print(c.Back.LIGHTRED_EX + '                     ' + c.Style.RESET_ALL)
print(c.Back.LIGHTBLACK_EX + '                     ' + c.Style.RESET_ALL)
print(c.Back.LIGHTMAGENTA_EX + '                     ' + c.Style.RESET_ALL)
print(c.Back.LIGHTGREEN_EX + '                     ' + c.Style.RESET_ALL)