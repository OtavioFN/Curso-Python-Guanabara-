#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
name = str(input('Digite uma frase: ')).strip()
print(f'A letra "a" aparece \033[31m{name.lower().count("a")}\033[0m vezes')
print(f'A letra "a" aparece pela primeira vez na posição \033[32m{name.lower().find("a")+1}\033[0m')
print(f'A letra "a" aparece pela última vez na posição \033[33m{name.lower().rfind("a")+1}\033[0m')