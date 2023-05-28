def linha():
    return '-' * 42

def leiaInt(ask):
    while True:
        try:
            num = int(input(ask))
        except (ValueError,TypeError):
            print('Esse número é inválido')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar um número')
            return 0
        else:
            return num

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for c,item in enumerate(lista):
        print(f'{c+1} - {item}')
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc
