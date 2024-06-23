lista = []
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        lista.append(num)
    else:
        soma = sum(lista)
        print(f'Você digitou {lista} e a soma entre eles foi de {soma}.')
        break
