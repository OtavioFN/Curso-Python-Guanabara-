# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”

'''city = str(input('Em qual cidade você nasceu?: ')).lower().strip()
splited_city = city.split()
print('santo' in splited_city[0])'''

#Ou

city = str(input('Em qual cidade você nasceu?: ')).strip()
Santo_CITY = city[:5].upper() == 'SANTO'
if  (city[:5].upper() == 'Santo') == True:
    print(f'\033[34m{city[:5].upper() == "SANTO"}\033[0m')
else:
    print(f'\033[31m{city[:5].upper() == "SANTO"}\033[0m')
