distancia = int(input('Qual é a distância da sua viagem? Km'))
preco = distancia * 0.50
preco200 = distancia * 0.45

if distancia <= 200:
    print (f'A sua viagem vai custar R${preco}')

else:
    print (f'A sua viagem vai custar R${preco200}')
