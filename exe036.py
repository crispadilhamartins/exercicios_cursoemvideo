valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salario mensal: '))
anos = int(input('Digite quantos anos de financiamento: '))

parcelas = valor_casa / (anos *12)
salario30 = salario * 30 /100

if parcelas <= salario30:
    print(f'As parcelas ficaram em R${parcelas:.2f}, seu emprestimo foi aprovado!')
else:
    print (f'O imprestimo não foi aprovado! Sua parcela de R${parcelas:.2f} iria passar o limite de 30% do seu salario!')