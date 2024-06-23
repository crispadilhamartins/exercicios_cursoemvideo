import random
import time

def rolar_dado():
    return random.randint(1, 6)

resultados = {}

for jogador in range (1, 5):
    resultados[f'Jogador {jogador}'] = rolar_dado()

for jogador, resultado in resultados.items():
    print(f'{jogador} Tirou: {resultado}')
    time.sleep(1)

print('-=' *30)
print('===RANKING DOS JOGADORES===')

resultados_ordenados = dict(sorted(resultados.items(), key=lambda item: item[1], reverse=True))

posicao = 1
for jogador, resultado in resultados_ordenados.items():
    print(f'{posicao}º {jogador}: {resultado}')
    posicao += 1
    time.sleep(1)

vencedor = max(resultados_ordenados, key=resultados_ordenados.get)
print(f'\nO vencedor é {jogador} com o número: {resultados_ordenados[vencedor]}')
