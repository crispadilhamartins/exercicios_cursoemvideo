palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print (f'\nNa palavra {p.upper()} temos ', end='')
    for vogal in p:
        if vogal in 'aeiou':
            print(vogal.upper(), end=' ')