prestaçao = float(input('Valor da prestação\nR$ '))
dias_em_atraso = int(input('Digite a quantidade de dias em atraso: '))
def Pagamento():
    print('Sistema de prestações')
    prestaçao = float(input('QValor da prestação\nR$ '))
    dias_em_atraso = int(input('Digite a quantidade de dias em atraso: '))
    while True:

        if dias_em_atraso == 0:
            print(f'O valor da prestação será de R$ {prestaçao} !')
        elif dias_em_atraso > 0:
            ValorPagamento()
        elif prestaçao == 0:
            print('Programa encerrado')
            break
        


def ValorPagamento():
    global prestação, dias_em_atraso

    prestação_nova = prestaçao + (3/100 * prestaçao) + (1/1000 * prestaçao) * dias_em_atraso
    print(f'Você pagará R$ {prestação_nova} em sua prestação!')
    Pagamento()
    
if __name__ == '__main__':
    Pagamento()