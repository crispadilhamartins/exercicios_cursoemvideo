def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos anlunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com varias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r

#Programa principal
resp = notas(5.5, 2.5, 3.5, 10, sit=True)
help(notas)