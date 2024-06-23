lista = []
pessoas = []
pesadas = []
leves = []
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    pessoas.append(nome)
    pessoas.append(peso)
    lista.append(pessoas[:])
    pessoas.clear()
    print('Cadastrado com sucesso!')

    escolha = str(input('Quer continuar? [S/N]')).upper().strip()
    if escolha == 'S':
        print('Proximo cadastro:')
        continue
    else:
        print('Ok, vamos finalizar o programa!')
        break

print(f'Foram cadastradas {len(lista)} pessoas no total!')

if lista:
    max_peso = max(lista, key=lambda x: x[1])[1]
    min_peso = min(lista, key=lambda x: x[1])[1]

    pesadas = [p for p in lista if p[1] == max_peso]
    leves = [p for p in lista if p[1] == min_peso]

    print(f'As pessoas mais pesadas têm {max_peso}Kg: ')
    for p in pesadas:
        print(f'{p[0]} com {p[1]}Kg.')
    print(f'As pessoas mais leves têm {min_peso}Kg: ')
    for p in leves:
        print(f'{p[0]} com {p[1]}Kg.')
