custo = float(input('Preço das compras: '))

print ('''
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    print (f'Sua compra de R${custo:.2f} vai custar R${custo - (10 /100 *custo):.2f}. 10% de desconto')
elif opcao == 2:
    print (f'Sua compra de R${custo:.2f} vai custar R${custo - (5 /100 *custo):.2f}. 5% de desconto')
elif opcao == 3:
    print (f'Sua compra vai custar R${custo:.2f}')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas >= 3:
        print (f'Sua compra de R${custo:.2f} vai custar R${custo + (20 /100 *custo):.2f}. 20% de juros')


