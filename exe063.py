n = int(input('Quantos termos você quer mostrar? '))

fib_sequence = [0,1]
i = 2

while i < n:
    next_num = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_num)
    i += 1

print(f'A sequencia de Fibonacci com os {n} primeiros termos é: {fib_sequence} FIM',end='')