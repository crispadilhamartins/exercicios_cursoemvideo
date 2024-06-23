a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
n = 1
termo_atual = a1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while n <= total:
            print(f'{termo_atual} - ', end='')
            termo_atual += r
            n += 1

    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('FIM')
print(f'Progressão finalizada. foram mostrados {total} termos ao todo!')