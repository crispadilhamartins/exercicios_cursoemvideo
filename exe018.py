import math

angulo = float(input('Digite um ângulo que você deseja: '))
rad = math.radians(angulo)

print (f'O angulo de {angulo} tem o SENO de {math.sin(rad):.2f} \nO ângulo de {angulo} tem o COSSENO de {math.cos(rad):.2f} \nO ângulo de {angulo} tem a TANGENTE de {math.tan(rad):.2f}')