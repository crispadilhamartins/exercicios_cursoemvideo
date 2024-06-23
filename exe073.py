'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''

classificacao = ['Athletico-PR', 'Bahia', 'Flamengo', 'Botafogo', 'São Paulo', 'Cruzeiro', 'Atletico-MG', 'Bragantino', 'Palmeiras', 'Internacional']

print(f'Lista de times do Campeonato Brasileiro: {classificacao}')
print(f'Os 5 primeiros são {classificacao[0:5]}')
print(f'Os 4 ultimos são {classificacao[-4:]}')
print(f'Times em ordem alfabética: {sorted(classificacao)}')
print(f'O Flamengo está na {classificacao.index("Flamengo")+1}ª posição.')