#Faça um programa que leia o ano de nascimento de um jovem e informe, 
#de acordo com a sua idade,
#se ele ainda vai se alistar ao serviço militar, 
#se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano_atual = date.today().year
genero = str(input('Informe seu gênero: (M) para masculino e (F) para feminino\n')).upper()
if genero == 'F':
    print('Não é obrigatório mulheres realizarem o alistamento militar!')
elif genero == 'M':
    ano_nascimento = int(input('Informe o seu ano de nascimento: '))
    print(f'Você tem {ano_atual - ano_nascimento} em {ano_atual}')
    idade = ano_atual - ano_nascimento
    if idade < 18:
        if 18 - idade == 1:
            print(f'Ainda falta {18 - idade} ano para você se alistar no exército')
        else:
            print(f'Ainda faltam {18 - idade} anos para você se alistar no exército')
        print(f'Seu alistamento será em {ano_atual + (18 - idade)}')
    if idade > 18:
        if idade - 18 == 1:
            print(f'Você deveria ter se alistado há {idade - 18} ano!')
        else:
            print(f'Você deveria ter se alistado há {idade - 18} anos!')
        print(f'Seu alistamento foi em {ano_atual - (idade - 18)}')
    if idade == 18:
        print('Você deve se alistar imediatamente!')
else:
    print('Resposta inválida, tente novamente!')
