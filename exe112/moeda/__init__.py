def aumentar(valor = 0, quantidade =10):
    return valor + (valor * quantidade /100)
    '''
    -> Calula o aumento de 10% de um determinado valor retornando um resultado.
    :param valor: o valor que se quer fazer o calculo
    :param quantidade =10: 10% de aumento
    :return: O valor calculado. 
    '''

def diminuir(valor = 0, quantidade =10):
    return valor - (valor * quantidade / 100)

def dobrar(valor = 0):
    return valor *2

def metade(valor = 0):
    return valor /2

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',') 