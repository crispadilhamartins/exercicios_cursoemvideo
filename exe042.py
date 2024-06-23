#2 lados iguais = isósceles
# todos os lados = equilátero
# todos diferentes = escaleno

a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento :'))

if a+b > c and b+c > a and a+c > b:
    print ('Pode formar um triangulo!')
    if a == b or b == c or c == a:
        print ('Tipo: ISÓSCELES')
    if a == b and b == c and c == a:
        print ('Tipo: EQUILÁTERO')
    if a != b and b != c and c != a:
        print ('Tipo: ESCALENO')

else:
    print ('Não pode formar um triangulo!')
