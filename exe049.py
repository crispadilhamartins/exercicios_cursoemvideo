valor = int(input('Digite um número para ver sua tabuada: '))

print (f'Tabuada do numero {valor}:')
for i in range(1, 11):
    resultado = valor * i
    print (f'{valor} X {i} = {resultado}')
