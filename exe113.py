def leiaInt():
    while True:
        try:
            valor = int(input('Digite um numero inteiro: '))
            return valor
        except ValueError:
            print('\033[91mValor inválido. Por favor, digite um número inteiro.\033[0m')
numero = leiaInt()
print(f'Voce digitou o numero inteiro: {numero}')