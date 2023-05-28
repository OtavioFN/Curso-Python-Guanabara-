'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. 
Importante: use cores.'''

import colorama
colorama.init()
from time import sleep

while True:
    print(colorama.Back.GREEN)
    command = str(input('Informe o comando que deseja ser informado ou digite FIM para encerrar o programa: ')).strip()
    print(colorama.Style.RESET_ALL)
    if 'FIM' in command:
        break
    else:
        print(colorama.Back.WHITE)
        help(command)
        print(colorama.Style.RESET_ALL)
print(colorama.Fore.BLUE + 'Programa encerrado' + colorama.Style.RESET_ALL)

