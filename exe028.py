import time
import random

print ('Vou pensar em um número entreo 0 e 5. Tente adivinhar...')

num = int(input('Em qual número eu pensei? '))
sorte = random.randint(0,5)

print ('Processando')
time.sleep(3)

if sorte == num :
    print (f'Você chutou {num} e o numero correto é {sorte}, parabêns!')

else:
    print (f'Você chutou {num} e o numero correto é {sorte}, você errou!')