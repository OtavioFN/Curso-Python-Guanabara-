'''Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com.br')
except urllib.error.URLError: # ou só o except
    print('Deu erro')
else:
    print('Tudo Ok')
    print(site.read()) # ler o conteúdo do dite