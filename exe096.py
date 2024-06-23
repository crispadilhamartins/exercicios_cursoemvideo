def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno {larg}x{comp} é {a}m².')


print('Controle de Terrenos')
print('-='*25)
l = float(input('Largura: (m) '))
c = float(input('Comprimento: (m)'))
area(l, c)
