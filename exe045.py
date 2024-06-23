import random
import time

print ('0 - PEDRA')
print ('1 - PAPEL')
print ('2 - TESOURA')

itens = ('Pedra', 'Papel', 'Tesoura')

cpu = random.randint(0,2)

jogada = int(input('Qual é a sua jogada? '))
print ('JO')
time.sleep(.5)
print ('KEN')
time.sleep(.5)
print ('PO!!!')
time.sleep(.5)

print ('-=' * 10)
print (f'CPU: {itens[cpu]}')
print (f'Você: {itens[jogada]}')
print ('-=' * 10)

if jogada == cpu:
    print('EMPATE!')

elif jogada == 0 and cpu == 2:
    print ('VOCÊ VENCEU!')

elif jogada == 1 and cpu == 0:
    print ('VOCÊ VENCEU!')

elif jogada == 2 and cpu == 1:
    print ('VOCÊ VENCEU!')

else:
    print ('VOCÊ PERDEU!')
