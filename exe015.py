#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.#

dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quandos KM foram percorridos? '))

print (f'A diaria do carro ficou em R${dias *60} mais R${km *0.15} por KM. O total é de R${(dias *60) + (km *0.15):.2f}')