from datetime import date
maior = 0
menor = 0
for pessoa in range (1, 8):
    ano = int(input('Digite o ano: '))

    data_atual = date.today().year
    idade = data_atual - ano

    if idade >= 18:
        print (f'A {pessoa}ª pessoa é maior de idade!')
        maior += +1


    else:
        print (f'A {pessoa}ª pessoa é menor de idade!')
        menor += +1

print (f'No total tivemos {maior} pessoa maiores de idade!')
print(f'E tambem tivemos {menor} pessoas menores de idade!')
