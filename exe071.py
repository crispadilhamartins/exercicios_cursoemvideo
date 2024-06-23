# Lista das cédulas disponíveis
cedulas = [200, 100, 50, 20, 10, 5, 2, 1]
quantidade_cedulas = {}

# Solicita ao usuário que insira um valor em reais
valor = int(input("Digite o valor em reais a ser distribuído: "))

# Distribuição das cédulas
for cedula in cedulas:
    quantidade = valor // cedula
    if quantidade > 0:
        quantidade_cedulas[cedula] = quantidade
        valor -= quantidade * cedula

# Exibe a distribuição das cédulas
print("Distribuição das cédulas:")
for cedula, quantidade in quantidade_cedulas.items():
    print(f"Cédulas de R${cedula}: {quantidade}")
