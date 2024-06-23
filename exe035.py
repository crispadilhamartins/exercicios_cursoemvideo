print('Analisador de Triângulos!')

a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a+b > c and a+c > b and b+c > a:
    print (f'Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print(f'Os segmentos acima NÃO PODEM FORMAR um triângulo! ')
