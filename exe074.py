import random
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9,10)#Tupla imutavel
sorteio = random.sample(numeros , 5)
sorteio_tupla = tuple(sorteio)#converte uma lista para uma tupla
maior = max(sorteio_tupla)
menor = min(sorteio_tupla)
print(sorteio)
print(f'O maior numero sorteado é {maior}')
print(f'O menor numero sorteado é {menor}')
