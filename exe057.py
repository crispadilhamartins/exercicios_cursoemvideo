import random

print ('Sou seu computador \nAcabei de pensar em um número ente 0 e 10. \nSerá que você consegue adivinhar qual foi?')
sorte = random.randint(1, 10)
contagem = 0
acertou = False

while not acertou:
    num = int(input('Qual é o seu palpite? '))
    contagem += 1
    if sorte < num:
            print ('Menos... Tente novamente.')
    elif sorte > num:
            print ('Mais... Tente novamente.')
    else:
        acertou = True
        print(f'Você acertou na {contagem}º tentativa. Parabéns!')
        break
