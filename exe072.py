from num2words import num2words
numero = int(input('Digite um número: '))
while True:
    if numero > 20:
        print('O número tem que ser menor que 20. \nTente novamente!')
        numero = int(input('Digite um número: '))
    else:
        num_ptbr = num2words(numero, lang='pt-br')
        print(num_ptbr)
        break