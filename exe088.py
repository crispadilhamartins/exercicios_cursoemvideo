print('-'*30)
print('JOGA NA MEGA SENA')
print('-'*30)

import random
from time import sleep

'''nvezes = int(input('Quantos jogos você quer fazer? '))

resultado = []

for _ in range(nvezes):
    sorteio = random.sample(range(1, 61), 6)
    resultado.append(sorteio)
for i, resultado in enumerate(resultado, start=1):
    print(f'Sorteio{i}: {sorted(resultado)}')
'''
lista = []
jogos = []
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = random.randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=' *3, f'SORTEANDO {quant} JOGOS ', '=' *3)

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' *5, 'Boa sorte', '-=' *3)
