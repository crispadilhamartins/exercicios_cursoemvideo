import cadastrar
import listar
from time import sleep

def exibir_menu():
    print('Sistemas de Cadastro de Pessoas')
    sleep(.5)
    print('[1] - Cadastrar nova pessoa')
    print('[2] - Ver lista de pessoas cadastradas')
    print('[3] - Limpar lista de pessoas cadastradas')
    print('[0] - Sair')
    escolha = input('Escolha uma opção: ')
    return escolha

def main():
    while True:
        escolha = exibir_menu()
        if escolha == '1':
            cadastrar.cadastrar_pessoas()
        elif escolha == '2':
            listar.listar_pessoas()
        elif escolha == '3':
            listar.limpar_lista()
        elif escolha == '0':
            print('Saindo do programa')
            sleep(.3)
            print('Programa encerrado!')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    main()
    