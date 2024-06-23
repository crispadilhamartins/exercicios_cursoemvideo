valores = []
pares = []
impares = []

while True:
    try:
        valor = int(input('Digite um valor: '))
        valores.append(valor)

    except ValueError:
        print('Valor inválido, digite um número inteiro!')
        continue

    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

    while True:
        
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()
        if escolha == 'S':
            break
        elif escolha =='N':
            print('Ok, estamos finalizando o programa!')
            print('Seu resultado vai estar logo abaixo')
            break
        else:
            print('Valor inválido, digite "S" para SIM e "N" para NÃO.')
            continue
    if escolha == 'N':
        break

print(f'Valores: {valores}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')