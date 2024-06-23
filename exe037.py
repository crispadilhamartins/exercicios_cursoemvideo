num = int(input('Digite um numero inteiro: '))

print ('Escolha uma das opções abaixo para conversão: \n[ 1 ] Converter em BINÁRIO \n[ 2 ] Converter em OCTAL \n[ 3 ] Converter em HEXADECIMAL')

escolha = int(input('Sua escolha: '))

if escolha == 1:
    print (f'O número {num} em BINÁRIO fica assim: {bin(num)[2:]}')
elif escolha == 2:
    print (f'O número {num} em OCTAL fica assim: {oct(num)[2:]}')
elif escolha == 3:
    print (f'O número {num} em HEXADECIMAL fica assim: {hex(num)[2:]}')
else:
    print ('Escolha inválida!')