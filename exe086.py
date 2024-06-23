# Criação de uma matriz 3x3 vazia
matriz = []

# Preenchendo a matriz com valores inseridos pelo usuário
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Insira o valor para a posição [{i}][{j}]: '))
        linha.append(valor)
    matriz.append(linha)

# Exibindo a matriz
for linha in matriz:
    print(linha)
