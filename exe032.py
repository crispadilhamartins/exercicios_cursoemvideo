from calendar import isleap
from datetime import date

ano = int(input('Digite o ano, vou dizer se é ou não é bissexto! Ou digite 0 para saber seu ano atual! '))

if ano == 0:
    ano = date.today().year

if isleap(ano) == True:
    print (f'O ano {ano} é Bissexto!')

else:
    print (f'O ano {ano} não é Bissexto!')