from moeda import aumentar, diminuir, dobrar, metade, moeda
from time import sleep

print('Olá, Eu me chamo Josh, sua calculador vitural.')
nome = str(input('Como eu posso lhe chamar? '))
print(f'Olá {nome}, vamos começar o programa')
sleep(.7)
while True:
    valor = float(input('Digite um valor R$ '))

    print('-=' *20)
    print("""
    [1] ¬ Aumenta 10% do valor
    [2] ¬ Diminui 10% do valor
    [3] ¬ Dobra o valor
    [4] ¬ Retira a metade do valor
    """)
    print('-=' *20)


    while True:
        escolha = int(input('Escolha uma das opções acima: '))

        if escolha == 1:
            valor = aumentar(valor)
            print(f'Aumentando 10% seu valor fica {moeda(valor)}')
            break

        elif escolha == 2:
            valor = diminuir(valor)
            print(f'Diminuindo 10% seu valor fica {moeda(valor)}')
            break
            

        elif escolha == 3:
            valor = dobrar(valor)
            print(f'O dobro fica {moeda(valor)}')
            break
        elif escolha == 4:
            valor = metade(valor)
            print(f'A metade fica {moeda(valor)}')
            break
    
        else:
            print('Escolha inválida, Digite um numero de 1 a 4.')
        continue
    continua = str(input('Deseja Continuar? S/N: '))

    if continua in 'Ss':
        continue
    elif continua in 'Nn':
        print('Ok, encerrando programa') 
        sleep(1)
        print('Programa encerrado. Obrigado!')
        break

    
