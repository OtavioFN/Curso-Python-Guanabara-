total_humanas = 0
total_saude = 0
total_exatas = 0
total_homem = 0
total_mulher = 0
aprovados_homem = 0
reprovados_homem = 0
aprovados_mulher = 0
reprovados_mulher = 0
aprovados_exatas = 0
reprovados_exatas = 0
aprovados_saude = 0
reprovados_saude = 0
aprovados_humanas = 0
reprovados_humanas = 0
aprovados_geral = 0
reprovados_geral = 0
for i in range(6):
    situaçao = str(input('Você foi aprovado? [S/N] ')).strip().upper()
    genero = str(input('Informe seu gênero: [M/F] ')).strip().upper()
    curso = str(input('Informe seu curso: [E - Exatas / S - Saúde / H - Humanas] ')).strip().upper()
    if situaçao == 'S':
        aprovados_geral += 1
    if situaçao == 'N':
        reprovados_geral += 1
    if situaçao == 'S' and curso == 'E':
        aprovados_exatas += 1
        total_exatas += 1
    if situaçao == 'N' and curso == 'E':
        reprovados_exatas += 1
        total_exatas += 1
    if situaçao == 'S' and curso == 'S':
        aprovados_saude += 1
        total_saude += 1
    if situaçao == 'N' and curso == 'S':
        reprovados_saude += 1
        total_saude += 1
    if situaçao == 'S' and curso == 'H':
        aprovados_humanas += 1
        total_humanas += 1
    if situaçao == 'N' and curso == 'H':
        reprovados_humanas += 1
        total_humanas += 1
    if situaçao == 'S' and genero == 'M':
        aprovados_homem += 1
        total_homem += 1
    if situaçao == 'N' and genero == 'M':
        reprovados_homem += 1
        total_homem += 1
    if situaçao == 'S' and genero == 'F':
        aprovados_mulher += 1
        total_mulher += 1
    if situaçao == 'N' and genero == 'F':
        reprovados_mulher += 1
        total_mulher += 1


if aprovados_geral != 0:
    print(f'A porcentagem de aprovados(as) no geral foi de {aprovados_geral*100/6:.1f}% ')
else:
    print('Não houve aprovados!')
if reprovados_geral != 0:   
    print(f'A porcentagem de reprovados(as) no geral foi de {reprovados_geral*100/6:.1f}% ')
else:
    print('Não houve reprovados!')
if total_exatas == 0:
    print('Não houve estudantes aplicados em exatas para sabermos a procentagem de aprovados!')
else:
    if aprovados_exatas == 0:
        print('Não houve aprovados em exatas!')
    else:
        print(f'A porcentagem de estudantes aprovados na área de exatas foi de {aprovados_exatas*100/total_exatas:.1f}% ')    
if total_exatas == 0:
    print('Não houve estudantes aplicados em exatas para sabermos a porcentagem de reprovados!')
else:
    if reprovados_exatas == 0:
        print('Não houve reprovados em exatas!')
    else:
        print(f'A porcentagem de estudantes reprovados na área de exatas foi de {reprovados_exatas*100/total_exatas:.1f}% ')
if total_saude == 0:
    print('Não houve estudantes aplicados na área de saúde para sabermos a porcentagem de aprovados!')
else:
    if aprovados_saude == 0:
        print('Não houve aprovados na área de saúde!')
    else:
        print(f'A porcentagem de estudantes aprovados na área de saúde foi de {aprovados_saude*100/total_saude:.1f}% ')
if total_saude == 0:
    print('Não houve estudantes aplicados na área de saúde para sabermos a porcentagem de reprovados!')
else:
    if reprovados_saude == 0:
        print('Não houve reprovados na área da sáude!')
    else:
        print(f'A procentagem de estudantes reprovados na área de saúde foi de {reprovados_saude*100/total_saude:.1f}% ')
if total_humanas == 0:
    print('Não houve estudantes aplicados em humanas para sabermos a porcentagem de aprovados!')
else:
    if aprovados_humanas == 0:
        print('Não houve aprovados em humanas!')
    else:
        print(f'A porcentagem de estudantes aprovados na área de humanas foi de {aprovados_humanas*100/total_humanas:.1f}% ')
if total_humanas == 0:
    print('Não houve estudantes aplicados em humanas para sabermos a porcentagem de reprovados!')
else:
    if reprovados_humanas == 0:
        print('Não houve estudantes reprovados em humanas!')
    else:
        print(f'A porcentagem de estudantes reprovados na área de humanas foi de {reprovados_humanas*100/total_humanas:.1f}% ')
if total_homem == 0:
    print('Não houve estudantes masculinos para sabermos a porcentagem de aprovados!')
else:
    if aprovados_homem == 0:
        print('Não houve estudantes masculinos aprovados!')
    else:
        print(f'A porcentagem de estudantes masculinos aprovados foi de {aprovados_homem*100/total_homem:.1f}% ')
if total_homem == 0:
    print('Não houve estudantes masculinos para sabermos a porcentagem de reprovados!')
else:
    if reprovados_homem == 0:
        print('Não houve estudantes masculinos reprovados!')
    else:
        print(f'A porcentagem de estudantes masculinos reprovados foi de {reprovados_homem*100/total_homem:.1f}% ')
if total_mulher == 0:
    print('Não houve estudantes femininas para sabermos a porcentagem de aprovadas!')
else:
    if aprovados_mulher == 0:
        print('Não houve estudantes femininas aprovadas!')
    else:
        print(f'A porcentagem de estudantes femininas aprovadas foi de {aprovados_mulher*100/total_mulher:.1f}% ')
if total_mulher == 0:
    print('Não houve estudantes femininas para sabermos a porcentagem de reprovadas!')
else:
    if reprovados_mulher == 0:
        print('Não houve estudantes femininas reprovadas!')
    else:
        print(f'A porcentagem de estudantes femininas reprovadas foi de {reprovados_mulher*100/total_mulher:.1f}% ')
