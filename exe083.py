expressao = input('Digite a expressão: ')
pilha = []

for char in expressao:
    if char == '(':
        pilha.append(char)
    elif char == ')':
        if not pilha:
            print("A expressão é inválida!")
            break
        pilha.pop()

if not pilha:
    print('A expressão é válida!')
else:
    print('A expressão é inválida!')