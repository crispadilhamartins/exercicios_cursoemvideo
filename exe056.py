mais_velho = 0
nome_velho = ''

maior_idade_homem = 0
media = 0
totmulher20 = 0
for c in range (1, 5):
    print (f'{c}ª PESSOA')

    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    media += (idade * c) /c

    if c == 1 and sexo in 'Mm':
        mais_velho = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    else:
        if mais_velho < idade:
            mais_velho = idade

    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

print (f'A media de idade do gupo é de {media/4} anos')
print (f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}')
print (f'Ao todo são {totmulher20} mulheres com menos de 20 anos')
