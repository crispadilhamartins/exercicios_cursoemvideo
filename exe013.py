print ('Olá, vamos calcular o novo salario com 15% de aumento!')

salario = float(input('Qual é o salário do funcionario? R$'))
novo = salario + (salario * 15/100)

print (f'Um funcionario que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${novo:.2f}')