'''Tratamento de erros e excessões

Exceção: "erro" que não se daria normalmente'''



'''print(x) #NameError

n = int(input('Número: ')) # ValueError
print(f'Você digitou o número {n}')

a = int(input('Numerador: ')) #ZeroDivisionError
b = int(input('Denominador: '))
r = a/b
print(f'O resultado é {r}')

lst = [3,6,4]
print(lst[3])'''

try: # Operação
    a = int(input('Numerador: ')) 
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou!')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
except Exception as erro: # Falhou
    print('Infelizmente tivemos um problema')
    print(f'Problema encontrado: {erro.__cause__}')
else: # Deu certo
    print(f'O resultado é {r:.1f}')
finally: # Ambos os casos: certo/falha
    print('Volte sempre! Muito obrigado')
