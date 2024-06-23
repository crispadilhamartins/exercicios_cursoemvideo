mais18 = 0
homens = 0
mulher_menos20 = 0

while True:
    print('CADASTRE UMA PESSOA')

    idade = int(input('Idade: '))
    if idade > 18:
        mais18 += 1

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo : [M/F] ')).upper().strip()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_menos20 += 1

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continua == 'N':
        break
    
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulher_menos20} mulheres com menos de 20 anos')
