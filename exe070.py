soma_total = 0
prod_maisd1000 = 0
menor = 0
cont = 0
barato = 0
while True:
    print('LOJA SUPER BARATÃO!')
    nome_prod = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    soma_total += preco
    if preco > 1000:
        prod_maisd1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome_prod
        
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break

print(f'O total gasto nas suas compras foi de R${soma_total:.2f}')
print(f'Você comprou {prod_maisd1000} produtos que custam mais de R$1.000')
print(f'O produto mais barato foi {barato} custa R${menor:.2f}')