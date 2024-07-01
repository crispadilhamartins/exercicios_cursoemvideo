def listar_pessoas():
    try:
        with open('pessoas.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.readlines()
            if conteudo:
                print("\nLista de pessoas cadastradas:")
                for linha in conteudo:
                    print(linha.strip())
            else:
                print('Nenhuma pessoa cadastrada.')
    except FileNotFoundError:
        print('Nenhuma pessoa cadastrada.')

def limpar_lista():
    with open('pessoas.txt', 'w', encoding='utf-8') as arquivo:
        pass
    print("\nA lista de pessoas cadastradas foi limpa.")
    print('')