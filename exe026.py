frase = str(input('Digite uma frese: ')).upper().strip(" ")


print (f'Aletra A aparece {frase.count('A')} vezes na frase.')
print (f'A primeira posição que ela aparece é {frase.find('A') + 1}')
print (f'A segunda prosição que ela aparece é {frase.rfind('A') + 1}')