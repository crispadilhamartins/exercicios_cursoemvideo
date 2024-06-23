peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = peso / (altura * altura)

if imc <= 18.5:
    print (f'IMC: {imc:.2f}. Classificação: Magreza')
elif imc <= 24.9:
    print (f'IMC: {imc:.2f}. Classificação: Normal')
elif imc <= 29.9:
    print (f'IMC: {imc:.2f}. Classificação: Sobrepeso')
elif imc <= 39.9:
    print (f'IMC {imc:.2f}. Classificação: Obesidade')
elif imc > 40.0:
    print (f'IMC {imc:.2f}. Classificação: Obesidade grave')
