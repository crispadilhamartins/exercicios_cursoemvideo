while True:
    try:
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))

        while True:
            print('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')

            opcao = int(input('Qual é a sua opção? '))

            if opcao == 1:
                soma = valor1 + valor2
                print (f'{valor1} + {valor2} = {soma}')
            elif opcao == 2:
                multiplica = valor1 * valor2
                print(f'{valor1} X {valor2} = {multiplica}')
            elif opcao == 3:
                if valor1 < valor2:
                    print(f'O valor {valor2} é maior que o valor {valor1}')
                elif valor1 > valor2:
                    print(f'O valor {valor2} é maior que o valor {valor1}')
                else:
                    print(f'O valor {valor1} é igual ao valor {valor2}')
            elif opcao == 4:
                break
            elif opcao == 5:
                print('Saindo do programa!')
                break
            else:
                print('Opção inválida. Por favor, escolha outra opção')
    except ValueError:
        print('Por favor, insira um número inteiro válido.')
