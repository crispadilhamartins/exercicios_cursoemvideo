def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro!\033[m')
        if ok:
            break
    return valor

#Programa principal
n = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número {n}')



"""
def leiaInt():
    while True:
        try:
            valor = int(input('Digite um numero inteiro: '))
            return valor
        except ValueError:
            print('\033[91mValor inválido. Por favor, digite um número inteiro.\033[0m')
numero = leiaInt()
print(f'Voce digitou o numero inteiro: {numero}')"""