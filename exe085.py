lista = [[],[]]
for v in range(1, 8):
    valor = int(input(f'Digite o {v}º valor: '))
    if v %2 == 0:
        lista[0].append(v)    
    else:
        lista[1].append(v)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram {lista[0]}.')
print(f'Os valores impares digitados foram {lista[1]}.')
