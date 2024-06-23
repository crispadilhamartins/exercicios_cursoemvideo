print('Olá, vamos calcular quanto de tinta você vai precisar para pintar sua parede, insira abaixo as informações.')

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))

print (f'Você vai usar um total de {(largura * altura) /2:.0f}L para pintar sua a area de {largura * altura}m²!')