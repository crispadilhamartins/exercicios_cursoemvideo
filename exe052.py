"""n = int(input('Digite um número: '))
mult = 0

for count in range(2,n):
    if (n % count == 0):
        print (f'Multiplo de {count}')
        mult += 1

if(mult==0):
    print('É primo!')
else:
    print(f'Tem {mult} multiplos acima de 2 e abaixo de {n}')"""

n = int(input('Digite um número: '))
tot = 0

for c in range(1, n + 1):
    if n % c == 0:
        tot += 1

print (f'O número {n} foi divisível {tot} vezes')
if tot == 2:
    print('É PRIMO')
else:
    print('NÃO É PRIMO')
