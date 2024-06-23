soma = 0
c = 0
for cont in range (1, 501, 2):
    if cont % 3 == 0:
        c = c + 1
        soma = soma + cont
print (f'A soma de todos os {c} valores solicitados é {soma}')