nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))


media = (nota1 + nota2) /2

if media < 5.0:
    print(f'Sua média ficou em {media}, Você está REPROVADO!')
elif media >= 5.0 and media <= 6.9:
    print(f'Sua média ficou em {media}, Você esta de RECUPERAÇÃO!')
else:
    print(f'Sua média ficou em {media}, Você está APROVADO!')
    