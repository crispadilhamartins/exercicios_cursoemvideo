def aumentar(valor = 0, quantidade =10):
    return valor + (valor * quantidade /100)


def diminuir(valor = 0, quantidade =10):
    return valor - (valor * quantidade / 100)

def dobrar(valor = 0):
    return valor *2

def metade(valor = 0):
    return valor /2

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',') 