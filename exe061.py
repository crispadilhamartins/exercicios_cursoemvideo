a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
n = 1

termo_atual = a1
termos = []
while n <= 10:
        termos.append(termo_atual)
        termo_atual += r
        n += 1

print(f'Os primeiros {n} termos da P.A são: {termos}')