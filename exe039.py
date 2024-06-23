from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nasc
print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}')

if idade == 18:
    print('Você tem que se alistar imediatamente!')

elif idade < 18:
    saldo = 18 -idade
    print(f'Ainda faltam {saldo} anos para o alistamento')

elif idade > 18:
    saldo = idade -18
    print(f'Você já deveria ter se alistado há {saldo} anos.')