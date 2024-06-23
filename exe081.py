'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

'''*****MEU CODIGO, FUNCIONANDO PELA METADE*****

valores = []

while True:
    try:
        n = int(input('Digite um valor: '))
        valores.append(n)

        escolha = str(input('Quer adicionar mais um valor? [S/N]')).upper().strip()
        if escolha == 'S':
            print('Ok, vamos continuar!')
            continue
        elif escolha == 'N':
            print('Tudo bem, Seu resultado está logo abaixo!')
            break   
    except ValueError:
        print('Valor inválido, Digite um número inteiro. Tente novamente.')


valores.sort(reverse=True)
print(f'Os valores digitados foram {valores}')'''


#CODIGO DO GUANABARA

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Você digitou {len(valores)} valores.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista!')
