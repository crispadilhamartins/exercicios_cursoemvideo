from math import sqrt
cat_oposto = float(input('Comprimento do cateto oposto: '))
cat_adjacente = float(input('Comprimento do cateto adjacente: '))
soma = (cat_adjacente**2) + (cat_oposto **2)

print (f'A hipotenusa vai medir {sqrt(soma)}')