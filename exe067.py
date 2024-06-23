while True:
    numero = int(input("Digite o número da tabuada: "))
    if numero < 0:
        print('Programa encerrado!')
        break
    i = 1
    while i <= 10:
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        i += 1
