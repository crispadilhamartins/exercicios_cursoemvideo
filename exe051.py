print ('10 TERMOS DE UMA PA')
termo1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo1 + (10 - 1) * razao

for c in range (termo1, decimo + razao, razao):
    print (c, end= ' > ')
print ('ACABOU')