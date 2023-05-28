'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
while True:
    choosed_number = int(input('Please choose a number between 0 and 20: '))
    while choosed_number > 20 or choosed_number < 0:
        choosed_number = int(input('Please choose a number between 0 and 20: '))
    print(numbers[choosed_number])
    resume = str(input('Would u like to continue? [Y/N]: ')).strip().upper()
    while resume not in 'YN':
        resume = str(input('Would u like to continue? [Y/N]: ')).strip().upper()
    if resume == 'N':
        break
print('SOFTWARE FINISHED')
        



'''#Guanabara

numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

while True:
    choosed_number = int(input('Please type a number between 0 and 20: '))
    if choosed_number > 0 and choosed_number < 20:
        break
print(numbers[choosed_number])'''