valores = [] 

while True:
    try:
        valor = int(input('Digite um valor: '))
        if valor in valores:
            print('Esse valor ja foi inserido. Por favor, insira um valor diferente!')
            continue
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    except ValueError:
        print('Entrada inválida! Por favor, insira um número inteiro.')
        continue

    while True:
        continuar = input('Quer continuar? [S/N] ').strip().upper()
        if continuar == 'S':
            break
        elif continuar == 'N':
            print('Vamos encerrar o programa! Obrigado!')
            valores.sort()
            print(f'Os valores inseridos foram {valores}')
            exit()
        else:
            print('Comando inválido, Digite "S" para SIM e "N" para NÃO')