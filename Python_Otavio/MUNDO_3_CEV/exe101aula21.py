'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

from datetime import date

ano_atual = date.today().year

def voto(ano):
    if ano_atual - ano >= 18:
        return f'Você tem {ano_atual - ano} anos, você precisa votar obrigatoriamente!'
    elif ano_atual - ano >= 16:
        return f'Você tem {ano_atual - ano} anos, seu voto é facultativo!'
    else:
        return f'Você tem {ano_atual - ano} anos, seu voto é proibido!'

print(voto(2005))
print(voto(1967))
print(voto(2007))
ano_nascimento = int(input('Informe o ano que você nasceu: '))
print(voto(ano_nascimento))