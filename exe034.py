salario = float(input('Digite o sálario que deseja consultar: '))

aumento10 = (10 /100) * salario
aumento15 = (15 /100) * salario

if salario > 1250:
    print (f'Quem ganhava R${salario:.2f} passa a ganhar R${salario + aumento10:.2f} com 10% de aumento! ')
if salario <= 1250:
    print (f'quem ganhava R${salario:.2f} passa a ganhar R${salario + aumento15:.2f} com 15% de aumento!')