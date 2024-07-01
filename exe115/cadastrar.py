def cadastrar_pessoas():
    from time import sleep
    nome = input('Digite o nome da pessoa: ').upper()
    idade = input('Digite a idade da pessoa: ')

    with open('pessoas.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"{nome}, {idade}\n")
    sleep(1)
    print(f'{nome} foi cadastrado(a) com sucesso!')
    print(' ')
    sleep(.5)