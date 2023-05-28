'''▸ O IMC (índice de massa corpórea) é uma medida que
pode ser utilizada para avaliar o peso de uma pessoa
em relação à sua altura, tendo a seguinte fórmula:

▸ Assim, construa um programa que leia o peso
e a altura do usuário e informe seu IMC e sua
classificação, de acordo com a tabela a seguir:

▸ Ao imprimir o IMC e classificação do usuário,
utilize as seguintes cores no terminal:

▸ Amarelo, para abaixo do peso ou sobrepeso

▸ Verde, para peso normal

▸ Vermelho, para obesidade grau I, II ou III'''


from colorama import Fore
from colorama import Style

peso = float(input('Informe seu peso em quilogramas: '))
altura = float(input('Informe sua altura em metros: '))
imc = peso/altura**2
if imc < 18.5:
    print(imc)
    print(Fore.YELLOW + 'Você está abaixo do peso!' + Style.RESET_ALL )
elif imc >= 18.5 and imc <= 24.9:
    print(f'{imc:.1f}')
    print(Fore.GREEN + 'Você está na faixa normal de peso!' + Style.RESET_ALL)
elif imc >= 25 and imc <= 29.9:
    print(f'{imc:.1f}')
    print(Fore.YELLOW + 'Voce está com sobrepeso!' + Style.RESET_ALL)
elif imc >= 30 and imc <= 34.9:
    print(f'{imc:.1f}')
    print(Fore.RED + 'Você está com Grau 1 de obesidade' + Style.RESET_ALL)
elif imc >= 35 and imc <= 39.9:
    print(f'{imc:.1f}')
    print(Fore.RED + 'Você está com Grau 2 de obesidade!' + Style.RESET_ALL)
elif imc >= 40:
    print(f'{imc:.1f}')
    print(Fore.RED + 'Você está com obesidade Mórbida!' + Style.RESET_ALL)
