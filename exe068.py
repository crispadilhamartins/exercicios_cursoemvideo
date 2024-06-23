import random
v = 0
while True:
    valor = int(input('Diga um valor de 1 a 10: '))
    cpu = random.randint(1, 10)
    soma = valor + cpu
    impar_par = ' '

    while impar_par not in 'PI':
        impar_par = str(input('Par ou impar? [P/I] ')).upper().strip()[0]
    if impar_par == 'P' and soma %2 == 0:
        print(f'Você jogou {valor} e a CPU jogou {cpu}. Total de {soma} DEU PAR')
        print('Você VENCEU')
        v += 1
        print('Jogue novamente!')

    elif impar_par == 'I' and soma %2 == 1:
        print(f'Você jogou {valor} e a CPU jogou {cpu}. Total de {soma} DEU IMPAR')
        print('Você VENCEU')
        v += 1
        print('Jogue novamente!')

    else:
        print(f'Você jogou {valor} e a CPU jogou {cpu}. Total de {soma} DEU impar')
        print('GAME OVER! Você perdeu!')
        print(f'Você ganhou {v} vezes!')
        break
