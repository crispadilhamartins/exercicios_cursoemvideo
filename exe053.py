def identificar_palindromo(frase):
    frase = frase.lower().replace(" ","").replace(",","").replace(".","")
    invertido = frase[::-1]

    if frase == invertido:
        return True
    else:
        return False

frase = input('Digite uma frase: ').strip().upper()
frase_invertida = frase[::-1]
if identificar_palindromo(frase):
    print (f"A frase {frase_invertida} é um palíndromo!")
else:
    print(f'A frase {frase_invertida} não é um palíndromo!')
