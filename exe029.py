speed = int(input('Qual a velocidade atual do carro? Km/h '))
limite = 80
multa = (speed - limite) *7
if speed > limite:
    print (f'Você foi multado, a multa vai custar R${multa:.2f}')

else:
    print ('Continue respeitando o limite da vida! Boa viagem!')

