maior = 0
menor = 0

for c in range (1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1: #Só executa o primero valor "SE(if) A ENTRADA(c) SER IGUAL(==) 1"
        maior = peso
        menor = peso
    else: #Ignora o primeiro if se não for a primeira entrada
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}Kg.')
print (f"O menor peso lido foi {menor}Kg.")
