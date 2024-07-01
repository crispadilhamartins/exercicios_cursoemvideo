def voto(anoNasc):
    import datetime
    idade = datetime.date.today().year - anoNasc
    if idade < 16:
        print(f'Com {idade} Anos. Não vota!')
    elif idade >= 16 and idade < 18 or idade > 65:
        print(f'Com {idade} Anos. Voto opcional!')
    else:
        print(f'Com {idade} Anos. Voto obrigatorio!')
        
anoNasc = int(input('Qual seu ano de nascimento? '))
voto(anoNasc)
